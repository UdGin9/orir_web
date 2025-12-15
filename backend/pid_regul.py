import control
import numpy as np


def pid_regul(F1, tau, k, F2, data):
    """
    Расчёт ПИД-регулятора по методу Циглера–Никольса.
    
    :param F1: постоянная времени объекта
    :param tau: время запаздывания
    :param k: коэффициент усиления объекта
    :param F2: коэффициент при s^2 в знаменателе передаточной функции объекта
    :param data: массив данных для масштабирования
    :return: t, y, Kp, Ki, Kd
    """
    num_pade, den_pade = control.pade(tau, n=3)
    delay_tf = control.TransferFunction(num_pade, den_pade)
    plant = control.TransferFunction([k], [F2, F1, 1])
    system_with_delay = control.series(plant, delay_tf)
    
    omega = np.logspace(-3, 3, 10000)
    mag, phase, _ = control.bode(system_with_delay, omega, plot=False)

    target_index = None
    for i in range(len(phase)):
        if phase[i] <= -np.pi:
            target_index = i
            break
    if target_index is None:
        raise ValueError("Система не достигает фазы -180° — невозможно определить Kcr")

    wc = omega[target_index]
    Kcr = 1.0 / mag[target_index]
    Tcr = 2 * np.pi / wc

    best_Kp, best_Ki, best_Kd = None, None, None

    for kp_factor in [0.45, 0.5, 0.55, 0.6]:
        for ti_factor in [0.4, 0.45, 0.5]:
            for td_factor in [0.1, 0.12, 0.15]:
                Kp = kp_factor * Kcr
                Ti = ti_factor * Tcr
                Td = td_factor * Tcr
                Ki = Kp / Ti
                Kd = Kp * Td

                Kp_tf = control.tf([Kp], [1])
                Ki_tf = control.tf([Ki], [1, 0])
                Kd_tf = control.tf([Kd, 0], [1])
                pid_controller = Kp_tf + Ki_tf + Kd_tf

                closed_loop = control.feedback(pid_controller * system_with_delay, 1)
                t_temp = np.linspace(0, 50, 1000)
                _, y_temp = control.step_response(closed_loop, T=t_temp)
                overshoot = (np.max(y_temp) - 1.0) * 100

                if 10 <= overshoot <= 20:
                    best_Kp, best_Ki, best_Kd = Kp, Ki, Kd
                    print(f"Найдены хорошие настройки PID: "
                          f"Kp={Kp:.3f}, Ki={Ki:.3f}, Kd={Kd:.3f}, "
                          f"перерегулирование={overshoot:.1f}%")
                    break
            if best_Kp is not None:
                break
        if best_Kp is not None:
            break

    if best_Kp is None:
        Kp = 0.6 * Kcr
        Ti = 0.5 * Tcr
        Td = 0.125 * Tcr
        Ki = Kp / Ti
        Kd = Kp * Td
        best_Kp, best_Ki, best_Kd = Kp, Ki, Kd
        print("Не удалось найти параметры с 10–20% перерегулированием, использованы стандартные.")

    Kp_tf = control.tf([best_Kp], [1])
    Ki_tf = control.tf([best_Ki], [1, 0])
    Kd_tf = control.tf([best_Kd, 0], [1])
    pid_controller = Kp_tf + Ki_tf + Kd_tf

    closed_loop = control.feedback(pid_controller * system_with_delay, 1)
    t, y = control.step_response(closed_loop, T=np.linspace(0, 50, 1000))
    y = max(data) * y

    negative_indices = np.where(y < 0)[0]
    if negative_indices.size > 0:
        last_neg_idx = negative_indices[-1]
        y = y[last_neg_idx + 1:]
        t = t[last_neg_idx + 1:]
    
    if tau > 0:
        n_zeros = int(np.floor(tau) + 1)
        if n_zeros > 0:
            t_zeros = np.arange(0, n_zeros)
            y_zeros = np.zeros(n_zeros)
            t_shifted = t + tau
            t = np.concatenate([t_zeros, t_shifted])
            y = np.concatenate([y_zeros, y])
    

    return t, y, best_Kp, best_Ki, best_Kd
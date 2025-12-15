import numpy as np
import control


def pi_regul(F1, tau, k, data):

    """
    Расчёт ПИ-регулятора по методу Циглера–Никольса с учётом запаздывания.
    
    :param F1: постоянная времени объекта (знаменатель: F1*s + 1)
    :param tau: время чистого запаздывания (сек)
    :param k: коэффициент усиления объекта
    :return: t, y — время и переходная характеристика замкнутой системы, Kp - П-коэффициент, Ki - интегральный коэффициент
    """

    num_pade, den_pade = control.pade(tau, n=3)
    delay_tf = control.TransferFunction(num_pade, den_pade)
    plant = control.TransferFunction([k], [F1, 1])
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
    gain_at_wc = mag[target_index]
    Kcr = 1.0 / gain_at_wc
    Tcr = 2 * np.pi / wc

    for kp_factor in [0.5, 0.55, 0.6, 0.65]:
        for ti_factor in [0.6, 0.65, 0.7, 0.75]:
            Kp = kp_factor * Kcr
            Ti = ti_factor * Tcr
            Ki = Kp / Ti

            pi_controller = control.tf([Kp], [1]) + control.tf([Ki], [1, 0])
            closed_loop = control.feedback(pi_controller * system_with_delay, 1)
            t, y = control.step_response(closed_loop, T=np.linspace(0, 50, 1000))

            overshoot = (np.max(y) - 1.0) * 100
            if 10 <= overshoot <= 20:
                print(f"Найдены хорошие настройки: Kp={Kp:.3f}, Ki={Ki:.3f}, перерегулирование={overshoot:.1f}%")
                break

    t, y = control.step_response(closed_loop, T=np.linspace(0, 50, 1000))
    y = max(data) * y

    negative_indices = np.where(y < 0)[0]
    if negative_indices.size > 0:
        last_neg_idx = negative_indices[-1]
        y = y[last_neg_idx + 1:]
        t = t[last_neg_idx + 1:]

    if tau > 0:
        n_zeros = int(np.floor(tau)) + 1
        if n_zeros > 0:
            t_zeros = np.arange(0, n_zeros)
            y_zeros = np.zeros(n_zeros)
            t = np.concatenate([t_zeros, t + tau])
            y = np.concatenate([y_zeros, y])

    return t, y, Kp, Ki
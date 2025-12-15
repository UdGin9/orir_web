import control 
import numpy as np


def reculculate_pid(F1, F2, k, Kp, Ki, Kd, tau, time, data):

    F1 = float(F1)
    F2 = float(F2)
    Kp = float(Kp)
    Ki = float(Ki)
    Kd = float(Kd)
    tau = float(tau)
    k= float(k)
    time = float(time)

    num_pade, den_pade = control.pade(tau, n=3)
    delay_tf = control.TransferFunction(num_pade, den_pade)
    plant = control.TransferFunction([k], [F2, F1, 1])
    system_with_delay = control.series(plant, delay_tf)

    Kp_tf = control.tf([Kp], [1])
    Ki_tf = control.tf([Ki], [1, 0])
    Kd_tf = control.tf([Kd, 0], [1])
    pid_controller = Kp_tf + Ki_tf + Kd_tf

    closed_loop = control.feedback(pid_controller * system_with_delay, 1)
    t, y = control.step_response(closed_loop, T=np.linspace(0, time, 1000))
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

    return t, y
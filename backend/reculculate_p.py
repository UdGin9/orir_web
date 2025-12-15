import control
import numpy as np

def reculculate_p(F1, tau, Kp,  k, time,  data):

    Kp = float(Kp)
    tau = float(tau)
    k= float(k)

    num_pade, den_pade = control.pade(tau, n=3)
    delay_tf = control.TransferFunction(num_pade, den_pade)
    plant = control.TransferFunction([k], [F1, 0])
    system_with_delay = control.series(plant, delay_tf)

    controller = control.tf([Kp], [1])
    closed_loop = control.feedback(controller * system_with_delay, 1)
    t, y = control.step_response(closed_loop, T=np.linspace(0, time, 1000))
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

    return t, y
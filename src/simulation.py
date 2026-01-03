import numpy as np

def create_f_matrix(phi_vals: list[float]) -> np.ndarray:
    order = len(phi_vals)
    f_matrix = np.zeros((order, order))
    f_matrix[0, :] = phi_vals

    for i in range(1, order):
        f_matrix[i, i-1] = 1

    return f_matrix

def calc_c_vals(eigvals: np.ndarray) -> np.ndarray:
    order = len(eigvals)
    c_vals = []

    for i in range(order):
        eigval = eigvals[i]
        denom = np.prod([eigval - eigvals[k] for k in range(order) if k != i])
        c_val = eigval**(order - 1) / denom
        c_vals.append(c_val)

    return np.array(c_vals, dtype=complex)

def calc_dyna_multi(c_vals: np.ndarray, eigvals: np.ndarray, lag: int) -> float:
    val = np.sum(c_vals * eigvals**lag)
    return np.real_if_close(val, tol=1e-8)

def simulate_dynamic_multipliers(phi_vals, lags):
    f_matrix = create_f_matrix(phi_vals)
    eigvals, _ = np.linalg.eig(f_matrix)
    c_vals = calc_c_vals(eigvals)

    dynamic_multis = []
    dynamic_multis_sim = []

    for lag in lags:
        dynamic_multis.append(calc_dyna_multi(c_vals, eigvals, lag))
        f_power = np.linalg.matrix_power(f_matrix, lag)
        dynamic_multis_sim.append(f_power[0, 0])

    return {
        "f_matrix": f_matrix,
        "eigvals": eigvals,
        "c_vals": c_vals,
        "dynamic_multis": np.array(dynamic_multis),
        "dynamic_multis_sim": np.array(dynamic_multis_sim)
    }

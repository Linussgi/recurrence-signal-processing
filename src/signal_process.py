import numpy as np
import matplotlib.pyplot as plt

# Global font size
FONTSIZE = 16

def frequency_response(c_vals, eigvals, num_points=500):
    omega = np.linspace(0, np.pi, num_points)
    H = np.zeros_like(omega, dtype=complex)

    for i, w in enumerate(omega):
        H[i] = np.sum(c_vals / (1 - eigvals * np.exp(-1j * w)))

    return omega, H

def plot_time_domain(lags, dynamic_multis, dynamic_multis_sim):
    fig, ax = plt.subplots(figsize=[12, 8])
    ax.plot(lags, dynamic_multis, "r-o", label="Analytical")
    ax.plot(lags, dynamic_multis_sim, "b--o", label="Simulated", ms=2)
    ax.set_xlabel("Lag", fontsize=FONTSIZE)
    ax.set_ylabel("Dynamic Multiplier", fontsize=FONTSIZE)
    ax.set_title("Dynamic Multipliers (Time Domain)", fontsize=FONTSIZE)
    ax.tick_params(axis="both", labelsize=FONTSIZE)
    ax.grid(True)
    ax.legend(fontsize=FONTSIZE)
    plt.show()

def plot_frequency_response(omega, H):
    fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=[12, 8], sharex=False)
    ax_mag.plot(omega, np.abs(H), "b", linewidth=2)
    ax_mag.set_ylabel("Magnitude", fontsize=FONTSIZE)
    ax_mag.set_title("Discrete Fourier Transforms", fontsize=FONTSIZE)
    ax_mag.tick_params(axis="both", labelsize=FONTSIZE)
    ax_mag.grid(True)

    ax_phase.plot(omega, np.angle(H), "r", linewidth=2)
    ax_phase.set_xlabel("Normalised Frequency [rad/sample]", fontsize=FONTSIZE)
    ax_phase.set_ylabel("Phase [rad]", fontsize=FONTSIZE)
    ax_phase.tick_params(axis="both", labelsize=FONTSIZE)
    ax_phase.grid(True)

    plt.tight_layout()
    plt.show()

def plot_pole_zero(eigvals):
    fig, ax = plt.subplots(figsize=[6, 6])
    ax.scatter(np.real(eigvals), np.imag(eigvals), marker="x", color="r", label="Poles")

    zeros = np.zeros(len(eigvals))
    ax.scatter(zeros, zeros, marker="o", facecolors="none", edgecolors="b", label="Zeros")

    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), "k--")

    ax.set_xlabel("Re", fontsize=FONTSIZE)
    ax.set_ylabel("Im", fontsize=FONTSIZE)
    ax.set_title("Pole-Zero Plot", fontsize=FONTSIZE)
    ax.tick_params(axis="both", labelsize=FONTSIZE)
    ax.grid(True)
    ax.axis("equal")
    ax.legend(fontsize=FONTSIZE)
    plt.show()

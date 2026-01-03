from simulation import simulate_dynamic_multipliers
from signal_process import plot_time_domain, frequency_response, plot_frequency_response, plot_pole_zero
from constants import PHI_VALUES, LAG_VALUES, OMEGA_POINTS

# Simulate dynamic multipliers
sim_results = simulate_dynamic_multipliers(PHI_VALUES, LAG_VALUES)

# Plot time-domain dynamic multipliers
plot_time_domain(LAG_VALUES, sim_results["dynamic_multis"], sim_results["dynamic_multis_sim"])

# Plot frequency response
omega, H = frequency_response(sim_results["c_vals"], sim_results["eigvals"], num_points=OMEGA_POINTS)
plot_frequency_response(omega, H)

# Plot pole-zero diagram
plot_pole_zero(sim_results["eigvals"])

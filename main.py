from src.data_handling import fetch_data, preprocess_data
from src.simulation import MonteCarloSimulator
from src.var_estimation import calculate_var
from src.visualization import plot_simulation_results

# Fetch and preprocess data
data = fetch_data(['AAPL', 'MSFT'], '2020-01-01', '2023-01-01')
processed_data = preprocess_data(data)

# Run Monte Carlo simulation
simulator = MonteCarloSimulator(processed_data)
simulator.run_simulation(num_simulations=10000, time_horizon=252)

# Calculate VaR
var_results = calculate_var(simulator.get_simulation_results(), confidence_level=0.95)

# Visualize results
plot_simulation_results(simulator.get_simulation_results(), asset_names=['AAPL', 'MSFT'])
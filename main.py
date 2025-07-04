from src.data_handling import fetch_data, preprocess_data
from src.simulation import MonteCarloSimulator
from src.var_estimation import calculate_var, calculate_cvar, calculate_sharpe_ratio, calculate_max_drawdown
from src.visualization import (
    plot_simulation_results,
    plot_portfolio_simulation,
    plot_correlation_matrix,
    plot_covariance_matrix,
    plot_return_distribution
)

# User parameters
tickers = ['AAPL', 'MSFT']
weights = [0.6, 0.4]  # Example: 60% AAPL, 40% MSFT
start_date = '2020-01-01'
end_date = '2023-01-01'
num_simulations = 5000
time_horizon = 252
confidence_level = 0.95

# Fetch and preprocess data
data = fetch_data(tickers, start_date, end_date)
processed_data = preprocess_data(data)

# Run Monte Carlo simulation
simulator = MonteCarloSimulator(processed_data)
simulator.run_simulation(num_simulations=num_simulations, time_horizon=time_horizon)

# Portfolio simulation
sim_results = simulator.get_simulation_results()  # shape: (sim, time, assets)
portfolio_paths = (sim_results * weights).sum(axis=2)  # Weighted sum across assets

# Risk metrics
var_results = calculate_var(portfolio_paths, confidence_level=confidence_level)
cvar_results = calculate_cvar(portfolio_paths, confidence_level=confidence_level)
sharpe = calculate_sharpe_ratio(portfolio_paths)
max_dd = calculate_max_drawdown(portfolio_paths)

# Visualizations
plot_simulation_results(sim_results, asset_names=tickers)
plot_portfolio_simulation(portfolio_paths)
plot_correlation_matrix(processed_data)
plot_covariance_matrix(processed_data)
plot_return_distribution(portfolio_paths)

# Print/report risk metrics
print(f"Portfolio VaR (95%): {var_results:.4f}")
print(f"Portfolio CVaR (95%): {cvar_results:.4f}")
print(f"Portfolio Sharpe Ratio: {sharpe:.4f}")
print(f"Portfolio Max Drawdown: {max_dd:.4f}")
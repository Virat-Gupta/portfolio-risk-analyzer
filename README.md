# Portfolio Risk Analyzer

## Overview
The Portfolio Risk Analyzer is a Python project that utilizes Monte Carlo Simulation to estimate the Value at Risk (VaR) of a portfolio. This tool is designed for financial analysts and risk managers to assess potential losses in their investment portfolios under various market conditions.

## Features
- **Data Handling**: Fetch and preprocess historical asset price data using the `yfinance` library.
- **Monte Carlo Simulation**: Simulate potential future asset prices to estimate risk.
- **Value at Risk (VaR) Calculation**: Calculate VaR based on simulation results.
- **Visualization**: Visualize simulation results and VaR estimates using Matplotlib and Seaborn.
- **Correlation and Covariance Analysis**: Optional analysis of asset returns to understand relationships and risk exposure.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd portfolio-risk-analyzer
pip install -r requirements.txt
```

## Usage
1. **Data Handling**: Use the `fetch_data` function from `data_handling.py` to retrieve historical price data for your assets.
2. **Run Simulation**: Create an instance of `MonteCarloSimulator` from `simulation.py` and call `run_simulation` to generate price paths.
3. **Calculate VaR**: Use the `calculate_var` function from `var_estimation.py` to compute the VaR from the simulation results.
4. **Visualize Results**: Utilize the plotting functions in `visualization.py` to visualize the simulation outcomes and VaR distribution.

## Example
```python
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
plot_simulation_results(simulator.get_simulation_results())
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
# Portfolio Risk Analyzer

A Python tool for simulating and analyzing portfolio risk using Monte Carlo simulation, historical data, and advanced risk metrics.  
Now with a user-friendly **web interface** powered by Streamlit!

---

## Features

- **Fetch historical data** for any set of tickers (via yfinance)
- **Monte Carlo simulation** of correlated asset price paths
- **Portfolio-level analysis** with custom weights
- **Risk metrics:** VaR, CVaR, Sharpe Ratio, Max Drawdown
- **Correlation & covariance matrix visualization**
- **Distribution plots** of simulated returns
- **Interactive web UI** (Streamlit) for easy use

---

## Quick Start

### 1. Install requirements

```sh
pip install -r requirements.txt
```

### 2. Run the web app

```sh
streamlit run app.py
```

Open the local URL shown in your terminal.

---

## Usage

- Select tickers, weights, date range, simulation count, and confidence level in the sidebar.
- Click **Run Analysis** to view:
  - Portfolio risk metrics (VaR, CVaR, Sharpe Ratio, Max Drawdown)
  - Simulated price paths for each asset
  - Simulated portfolio value paths
  - Correlation and covariance heatmaps
  - Distribution of simulated portfolio returns

---

## Project Structure

```
src/
  data_handling.py
  simulation.py
  var_estimation.py
  visualization.py
app.py
requirements.txt
README.md
```

---

## Example (Python API)

```python
from src.data_handling import fetch_data, preprocess_data
from src.simulation import MonteCarloSimulator
from src.var_estimation import calculate_var
from src.visualization import plot_simulation_results

data = fetch_data(['AAPL', 'MSFT'], '2020-01-01', '2023-01-01')
returns = preprocess_data(data)
simulator = MonteCarloSimulator(returns)
simulator.run_simulation(num_simulations=1000, time_horizon=252)
sim_results = simulator.get_simulation_results()
plot_simulation_results(sim_results, asset_names=['AAPL', 'MSFT'])
```

---

## Requirements

See `requirements.txt` for all dependencies.

---

## License

MIT License
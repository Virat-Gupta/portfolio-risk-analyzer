import streamlit as st
import numpy as np
import pandas as pd
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

st.title("Portfolio Risk Analyzer")

# Sidebar for user input
tickers = st.sidebar.multiselect("Select Tickers", ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA'], default=['AAPL', 'MSFT'])
weights = []
for t in tickers:
    w = st.sidebar.number_input(f"Weight for {t}", min_value=0.0, max_value=1.0, value=1.0/len(tickers))
    weights.append(w)
weights = np.array(weights)
if weights.sum() != 1.0 and len(weights) > 0:
    weights = weights / weights.sum()  # Normalize

start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
num_simulations = st.sidebar.slider("Number of Simulations", 100, 10000, 2000)
time_horizon = st.sidebar.slider("Time Horizon (days)", 30, 756, 252)
confidence_level = st.sidebar.slider("Confidence Level", 0.90, 0.99, 0.95)

if st.button("Run Analysis"):
    with st.spinner("Fetching data and running simulations..."):
        data = fetch_data(tickers, str(start_date), str(end_date))
        processed_data = preprocess_data(data)
        simulator = MonteCarloSimulator(processed_data)
        simulator.run_simulation(num_simulations=num_simulations, time_horizon=time_horizon)
        sim_results = simulator.get_simulation_results()
        portfolio_paths = (sim_results * weights).sum(axis=2)

        var_results = calculate_var(portfolio_paths, confidence_level=confidence_level)
        cvar_results = calculate_cvar(portfolio_paths, confidence_level=confidence_level)
        sharpe = calculate_sharpe_ratio(portfolio_paths)
        max_dd = calculate_max_drawdown(portfolio_paths)

    st.subheader("Risk Metrics")
    st.write(f"**Portfolio VaR ({int(confidence_level*100)}%)**: {var_results:.4f}")
    st.write(f"**Portfolio CVaR ({int(confidence_level*100)}%)**: {cvar_results:.4f}")
    st.write(f"**Portfolio Sharpe Ratio**: {sharpe:.4f}")
    st.write(f"**Portfolio Max Drawdown**: {max_dd:.4f}")

    st.subheader("Visualizations")
    for fig in plot_simulation_results(sim_results, asset_names=tickers):
        st.pyplot(fig)
    st.pyplot(plot_portfolio_simulation(portfolio_paths))
    st.pyplot(plot_correlation_matrix(processed_data))
    st.pyplot(plot_covariance_matrix(processed_data))
    st.pyplot(plot_return_distribution(portfolio_paths))
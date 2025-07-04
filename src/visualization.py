import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_portfolio_simulation(portfolio_paths, num_paths=20):
    """
    Plot a subset of simulated portfolio value paths and show mean and percentile bands.
    Returns the matplotlib figure object for Streamlit.
    """
    time = np.arange(portfolio_paths.shape[1])
    fig, ax = plt.subplots(figsize=(10, 5))
    for i in range(min(num_paths, portfolio_paths.shape[0])):
        ax.plot(time, portfolio_paths[i], color='gray', alpha=0.2)
    mean_path = portfolio_paths.mean(axis=0)
    ax.plot(time, mean_path, color='blue', label='Mean Path', linewidth=2)
    p5 = np.percentile(portfolio_paths, 5, axis=0)
    p95 = np.percentile(portfolio_paths, 95, axis=0)
    ax.fill_between(time, p5, p95, color='blue', alpha=0.15, label='5th-95th Percentile')
    ax.set_title("Simulated Portfolio Value Paths")
    ax.set_xlabel("Time Step (Days)")
    ax.set_ylabel("Normalized Portfolio Value")
    ax.legend()
    fig.tight_layout()
    return fig

def plot_simulation_results(results, asset_names=None, num_paths=20):
    """
    Plot simulated price paths for each asset in separate plots,
    including mean and percentile bands for clarity.
    Returns a list of matplotlib figure objects for Streamlit.
    """
    num_simulations, time_horizon_plus1, num_assets = results.shape
    time = np.arange(time_horizon_plus1)
    figs = []
    if asset_names is None:
        asset_names = [f"Asset {i+1}" for i in range(num_assets)]
    for asset in range(num_assets):
        fig, ax = plt.subplots(figsize=(10, 5))
        for i in range(min(num_paths, num_simulations)):
            ax.plot(time, results[i, :, asset], color='gray', alpha=0.2, linewidth=0.8)
        mean_path = results[:, :, asset].mean(axis=0)
        ax.plot(time, mean_path, color='blue', label='Mean Path', linewidth=2)
        p5 = np.percentile(results[:, :, asset], 5, axis=0)
        p95 = np.percentile(results[:, :, asset], 95, axis=0)
        ax.fill_between(time, p5, p95, color='blue', alpha=0.15, label='5th-95th Percentile')
        ax.set_title(f"Simulated Price Paths for {asset_names[asset]}")
        ax.set_xlabel("Time Step (Days)")
        ax.set_ylabel("Normalized Price")
        ax.legend()
        fig.tight_layout()
        figs.append(fig)
    return figs

def plot_correlation_matrix(returns):
    """
    Plot the correlation matrix of asset returns and return the figure for Streamlit.
    """
    corr = returns.corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Asset Correlation Matrix")
    fig.tight_layout()
    return fig

def plot_covariance_matrix(returns):
    """
    Plot the covariance matrix of asset returns and return the figure for Streamlit.
    """
    cov = returns.cov()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cov, annot=True, cmap='YlGnBu', ax=ax)
    ax.set_title("Asset Covariance Matrix")
    fig.tight_layout()
    return fig

def plot_return_distribution(portfolio_paths):
    """
    Plot the distribution of simulated portfolio returns and return the figure for Streamlit.
    """
    returns = portfolio_paths[:, -1] / portfolio_paths[:, 0] - 1
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(returns, bins=50, kde=True, ax=ax)
    ax.set_title("Distribution of Simulated Portfolio Returns")
    ax.set_xlabel("Return")
    ax.set_ylabel("Frequency")
    fig.tight_layout()
    return fig
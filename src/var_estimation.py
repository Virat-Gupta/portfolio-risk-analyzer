import numpy as np

def calculate_var(portfolio_paths, confidence_level=0.95):
    """
    Calculate the Value at Risk (VaR) from simulation results.

    Parameters:
    simulation_results (numpy.ndarray): Array of simulated asset prices.
    confidence_level (float): Confidence level for VaR calculation (default is 0.95).

    Returns:
    float: The calculated VaR value.
    """
    # Calculate losses (negative returns)
    returns = portfolio_paths[:, -1] / portfolio_paths[:, 0] - 1
    losses = -returns
    # Calculate the VaR at the specified confidence level
    var = np.percentile(losses, (1 - confidence_level) * 100)
    return var

def calculate_cvar(portfolio_paths, confidence_level=0.95):
    """
    Calculate the Conditional Value at Risk (CVaR) from simulation results.

    Parameters:
    simulation_results (numpy.ndarray): Array of simulated asset prices.
    confidence_level (float): Confidence level for CVaR calculation (default is 0.95).

    Returns:
    float: The calculated CVaR value.
    """
    returns = portfolio_paths[:, -1] / portfolio_paths[:, 0] - 1
    losses = -returns
    var = np.percentile(losses, (1 - confidence_level) * 100)
    cvar = losses[losses >= var].mean()
    return cvar

def calculate_sharpe_ratio(portfolio_paths, risk_free_rate=0.0):
    """
    Calculate the Sharpe Ratio from simulation results.

    Parameters:
    simulation_results (numpy.ndarray): Array of simulated asset prices.
    risk_free_rate (float): Risk-free rate for Sharpe Ratio calculation (default is 0.0).

    Returns:
    float: The calculated Sharpe Ratio.
    """
    returns = portfolio_paths[:, -1] / portfolio_paths[:, 0] - 1
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def calculate_max_drawdown(portfolio_paths):
    """
    Calculate the maximum drawdown from simulation results.

    Parameters:
    simulation_results (numpy.ndarray): Array of simulated asset prices.

    Returns:
    float: The calculated maximum drawdown.
    """
    # Calculate max drawdown for each simulation, then average
    max_dds = []
    for path in portfolio_paths:
        running_max = np.maximum.accumulate(path)
        drawdowns = (path - running_max) / running_max
        max_dds.append(drawdowns.min())
    return np.mean(max_dds)

def get_var_summary(var_results):
    """
    Generate a summary of VaR results.

    Parameters:
    var_results (list): List of VaR results from multiple simulations.

    Returns:
    dict: A summary containing mean, median, and standard deviation of VaR results.
    """
    var_summary = {
        'mean_var': np.mean(var_results),
        'median_var': np.median(var_results),
        'std_var': np.std(var_results)
    }
    return var_summary
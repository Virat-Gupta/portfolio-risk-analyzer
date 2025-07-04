import numpy as np

def calculate_var(simulation_results, confidence_level=0.95):
    """
    Calculate the Value at Risk (VaR) from simulation results.

    Parameters:
    simulation_results (numpy.ndarray): Array of simulated asset prices.
    confidence_level (float): Confidence level for VaR calculation (default is 0.95).

    Returns:
    float: The calculated VaR value.
    """
    # Calculate the losses
    losses = simulation_results[-1] - simulation_results
    # Calculate the VaR at the specified confidence level
    var = np.percentile(losses, (1 - confidence_level) * 100)
    return var

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
import matplotlib.pyplot as plt
import seaborn as sns

def plot_simulation_results(results, num_paths=20):
    """
    Plot a subset of simulated price paths for all assets on the same plot.
    results: np.ndarray of shape (num_simulations, time_horizon+1, num_assets)
    """
    num_simulations, time_horizon_plus1, num_assets = results.shape
    time = range(time_horizon_plus1)
    plt.figure(figsize=(12, 6))
    for asset in range(num_assets):
        for i in range(min(num_paths, num_simulations)):
            plt.plot(time, results[i, :, asset], alpha=0.3, label=f'Asset {asset+1}' if i == 0 else "")
    plt.title("Simulated Price Paths for All Assets")
    plt.xlabel("Time Step")
    plt.ylabel("Normalized Price")
    plt.legend()
    plt.show()

def plot_var_distribution(var_data):
    plt.figure(figsize=(10, 6))
    sns.histplot(var_data, bins=30, kde=True)
    plt.title('Value at Risk Distribution')
    plt.xlabel('Value at Risk')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()
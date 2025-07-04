import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_results(results, asset_names=None, num_paths=20):
    """
    Plot simulated price paths for each asset in separate plots,
    including mean and percentile bands for clarity.
    """
    num_simulations, time_horizon_plus1, num_assets = results.shape
    time = np.arange(time_horizon_plus1)
    if asset_names is None:
        asset_names = [f"Asset {i+1}" for i in range(num_assets)]
    for asset in range(num_assets):
        plt.figure(figsize=(10, 5))
        # Plot a subset of simulation paths
        for i in range(min(num_paths, num_simulations)):
            plt.plot(time, results[i, :, asset], color='gray', alpha=0.2, linewidth=0.8)
        # Plot mean path
        mean_path = results[:, :, asset].mean(axis=0)
        plt.plot(time, mean_path, color='blue', label='Mean Path', linewidth=2)
        # Plot 5th and 95th percentile bands
        p5 = np.percentile(results[:, :, asset], 5, axis=0)
        p95 = np.percentile(results[:, :, asset], 95, axis=0)
        plt.fill_between(time, p5, p95, color='blue', alpha=0.15, label='5th-95th Percentile')
        plt.title(f"Simulated Price Paths for {asset_names[asset]}")
        plt.xlabel("Time Step (Days)")
        plt.ylabel("Normalized Price")
        plt.legend()
        plt.tight_layout()
        plt.show()
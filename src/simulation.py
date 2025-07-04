import numpy as np

class MonteCarloSimulator:
    def __init__(self, returns):
        self.returns = returns
        self.simulations = None

    def run_simulation(self, num_simulations=10000, time_horizon=252):
        # Number of assets
        num_assets = self.returns.shape[1]
        # Initialize simulations: shape (num_simulations, time_horizon + 1, num_assets)
        self.simulations = np.zeros((num_simulations, time_horizon + 1, num_assets))
        last_prices = self.returns.iloc[-1]  # This should be the last known price, but you have returns, so use 1.0 as base

        # Calculate mean and covariance of returns
        mean_returns = self.returns.mean()
        cov_matrix = self.returns.cov()

        for i in range(num_simulations):
            prices = np.ones(num_assets)  # Start at 1.0 for each asset
            price_path = [prices.copy()]
            for _ in range(time_horizon):
                # Simulate correlated returns
                simulated_returns = np.random.multivariate_normal(mean_returns, cov_matrix)
                prices = prices * (1 + simulated_returns)
                price_path.append(prices.copy())
            self.simulations[i] = price_path

    def get_simulation_results(self):
        return self.simulations
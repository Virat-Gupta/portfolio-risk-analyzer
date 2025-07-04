import numpy as np

class MonteCarloSimulator:
    def __init__(self, returns):
        self.returns = returns
        self.simulations = None

    def run_simulation(self, num_simulations=1000, time_horizon=252):
        num_assets = self.returns.shape[1]
        mean_returns = self.returns.mean().values
        cov_matrix = self.returns.cov().values

        # Cholesky decomposition for correlated random numbers
        chol = np.linalg.cholesky(cov_matrix)

        # Generate all random numbers at once
        rand_normals = np.random.normal(size=(num_simulations, time_horizon, num_assets))
        correlated_randoms = rand_normals @ chol.T

        # Add mean to each step
        correlated_randoms += mean_returns

        # Start all simulations at 1.0
        prices = np.ones((num_simulations, time_horizon + 1, num_assets))
        for t in range(1, time_horizon + 1):
            prices[:, t, :] = prices[:, t - 1, :] * (1 + correlated_randoms[:, t - 1, :])

        self.simulations = prices

    def get_simulation_results(self):
        return self.simulations
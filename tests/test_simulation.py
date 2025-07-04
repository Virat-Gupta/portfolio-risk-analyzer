import unittest
from src.simulation import MonteCarloSimulator

class TestMonteCarloSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = MonteCarloSimulator()
        self.num_simulations = 1000
        self.time_horizon = 30

    def test_run_simulation(self):
        results = self.simulator.run_simulation(self.num_simulations, self.time_horizon)
        self.assertEqual(len(results), self.num_simulations)
        self.assertEqual(len(results[0]), self.time_horizon)

    def test_get_simulation_results(self):
        self.simulator.run_simulation(self.num_simulations, self.time_horizon)
        results = self.simulator.get_simulation_results()
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
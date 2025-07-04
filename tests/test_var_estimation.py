import unittest
from src.var_estimation import calculate_var, get_var_summary

class TestVarEstimation(unittest.TestCase):

    def setUp(self):
        self.simulation_results = [100, 102, 98, 105, 97, 110, 95, 101, 99, 104]
        self.confidence_level = 0.95

    def test_calculate_var(self):
        var = calculate_var(self.simulation_results, self.confidence_level)
        self.assertIsInstance(var, float)

    def test_get_var_summary(self):
        var_results = [calculate_var(self.simulation_results, cl) for cl in [0.90, 0.95, 0.99]]
        summary = get_var_summary(var_results)
        self.assertIsInstance(summary, dict)
        self.assertIn('VaR at 90%', summary)
        self.assertIn('VaR at 95%', summary)
        self.assertIn('VaR at 99%', summary)

if __name__ == '__main__':
    unittest.main()
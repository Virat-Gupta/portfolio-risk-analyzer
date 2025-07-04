import unittest
from src.visualization import plot_simulation_results, plot_var_distribution

class TestVisualization(unittest.TestCase):

    def test_plot_simulation_results(self):
        # Sample data for testing
        results = {
            'simulations': [[100, 102, 101], [100, 98, 99]],
            'mean': 100,
            'std_dev': 1.5
        }
        # Test if the function runs without errors
        try:
            plot_simulation_results(results)
            success = True
        except Exception as e:
            success = False
            print(f"Error: {e}")
        self.assertTrue(success)

    def test_plot_var_distribution(self):
        # Sample data for testing
        var_data = [0.01, 0.02, 0.015, 0.03]
        # Test if the function runs without errors
        try:
            plot_var_distribution(var_data)
            success = True
        except Exception as e:
            success = False
            print(f"Error: {e}")
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
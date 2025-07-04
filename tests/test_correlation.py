import unittest
import numpy as np
import pandas as pd
from src.correlation import calculate_correlation_matrix, visualize_correlation_matrix

class TestCorrelationFunctions(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = pd.DataFrame({
            'Asset1': [0.1, 0.2, 0.3, 0.4, 0.5],
            'Asset2': [0.5, 0.4, 0.3, 0.2, 0.1],
            'Asset3': [0.2, 0.3, 0.4, 0.5, 0.6]
        })

    def test_calculate_correlation_matrix(self):
        expected_correlation = np.array([
            [1.0, -1.0, 0.9],
            [-1.0, 1.0, -0.9],
            [0.9, -0.9, 1.0]
        ])
        correlation_matrix = calculate_correlation_matrix(self.data)
        pd.testing.assert_frame_equal(pd.DataFrame(correlation_matrix), pd.DataFrame(expected_correlation))

    def test_visualize_correlation_matrix(self):
        # This test will check if the function runs without errors
        correlation_matrix = calculate_correlation_matrix(self.data)
        try:
            visualize_correlation_matrix(correlation_matrix)
        except Exception as e:
            self.fail(f"visualize_correlation_matrix raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
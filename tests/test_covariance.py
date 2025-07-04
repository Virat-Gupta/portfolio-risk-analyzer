import unittest
import numpy as np
from src.covariance import calculate_covariance_matrix

class TestCovariance(unittest.TestCase):

    def setUp(self):
        self.data = np.array([
            [0.1, 0.2, 0.3],
            [0.2, 0.3, 0.4],
            [0.3, 0.4, 0.5]
        ])

    def test_calculate_covariance_matrix(self):
        expected_covariance = np.array([
            [0.01, 0.01, 0.01],
            [0.01, 0.01, 0.01],
            [0.01, 0.01, 0.01]
        ])
        result = calculate_covariance_matrix(self.data)
        np.testing.assert_array_almost_equal(result, expected_covariance, decimal=2)

if __name__ == '__main__':
    unittest.main()
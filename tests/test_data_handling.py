import unittest
from src.data_handling import fetch_data, preprocess_data
import pandas as pd

class TestDataHandling(unittest.TestCase):

    def test_fetch_data(self):
        tickers = ['AAPL', 'MSFT']
        start_date = '2020-01-01'
        end_date = '2020-12-31'
        data = fetch_data(tickers, start_date, end_date)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        data = pd.DataFrame({
            'Date': pd.date_range(start='2020-01-01', periods=5),
            'AAPL': [300, 305, 310, 315, 320],
            'MSFT': [200, 205, 210, 215, 220]
        })
        processed_data = preprocess_data(data)
        self.assertIn('Returns', processed_data.columns)
        self.assertFalse(processed_data['Returns'].isnull().any())

if __name__ == '__main__':
    unittest.main()
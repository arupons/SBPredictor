import unittest
from Predictor import Predictor


class PredictorTest(unittest.TestCase):

    def test_valid(self):
        result = Predictor().predict('aaa-123', '2019-04-08', '08:00')
        self.assertTrue(result['success'])

    def test_invalid_plate(self):
        result = Predictor().predict('aaa-123d', '2019-04-09', '08:00')
        self.assertFalse(result['success'])

    def test_invalid_date(self):
        result = Predictor().predict('aaa-123', '2019-04-40', '08:00')
        self.assertFalse(result['success'])

    def test_invalid_time(self):
        result = Predictor().predict('aaa-123', '2019-04-09', '28:00')
        self.assertFalse(result['success'])


if __name__ == '__main__':
    unittest.main()

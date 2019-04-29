import unittest
from Plate import Plate


class PlateTest(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(Plate().validate('ABC-123'))

    def test_invalid(self):
        self.assertFalse(Plate().validate('ABC-123d'))


if __name__ == '__main__':
    unittest.main()

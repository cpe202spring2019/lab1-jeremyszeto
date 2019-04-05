import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq_1(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == loc1)

    def test_eq_2(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Paris", 48.9, 2.4)
        self.assertFalse(loc == loc1)

    def test_eq_3(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = ("Paris", 48.9, 2.4)
        self.assertFalse(loc == loc1)

if __name__ == "__main__":
        unittest.main()

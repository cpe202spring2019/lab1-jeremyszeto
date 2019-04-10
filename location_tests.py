import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """tests if __repr__ prints expected output"""
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        """ tests if __eq__ functions as expected"""
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = ("Paris", 48.9, 2.4)
        loc4 = loc1


        self.assertFalse(loc == loc2)
        self.assertFalse(loc == loc3)
        self.assertTrue(loc == loc4)
        self.assertTrue(loc == loc1)


if __name__ == "__main__":
        unittest.main()

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
# tests for max_list_iter
    def test_max_list_iter_none(self):
        """check ValueError raised for None list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty(self):
        """check None returned for empty list"""
        self.assertIsNone(max_list_iter([]))

    def test_max_list_iter(self):
        """check for correct max with different number combinations"""
        self.assertEqual(max_list_iter([1,2,3]), 3)
        self.assertEqual(max_list_iter([1,3,2]), 3)
        self.assertEqual(max_list_iter([3,2,1]), 3)
        self.assertEqual(max_list_iter([2,2,3]), 3)
        self.assertEqual(max_list_iter([2,3,2]), 3)
        self.assertEqual(max_list_iter([3,2,2]), 3)
        self.assertEqual(max_list_iter([2,3,3]), 3)
        self.assertEqual(max_list_iter([3,2,3]), 3)
        self.assertEqual(max_list_iter([3,3,2]), 3)
        self.assertEqual(max_list_iter([3,3,3]), 3)
        self.assertEqual(max_list_iter([2.1, 3.1, 1]), 3.1)
        self.assertEqual(max_list_iter([-1,-2,-3]), -1)

# tests for reverse_rec
    def test_reverse_rec_none(self):
        """check ValueError raised for None list"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_reverse_rec_empty(self):
        """check [] returned for empty list"""
        self.assertEqual(reverse_rec([]), [])
    
    def test_reverse_rec(self):
        """check if list is reversed properly"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,2]),[2,1,1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([1.1,2.2,3.3]), [3.3,2.2,1.1])
        self.assertEqual(reverse_rec([1]), [1])

    def test_bin_search_none(self):
        """check ValueError raised for None list"""
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, list_val)

    def test_bin_search_empty_list(self):
        """check if None returned for empty list"""
        list_val = []
        self.assertIsNone(bin_search(0, 0, len(list_val)-1, list_val))

    def test_bin_search_no_target(self):
        """check if None returned for target not found"""
        list_val = [0,1,2,3,4]
        self.assertIsNone(bin_search(5, 0, len(list_val)-1, list_val))
        self.assertIsNone(bin_search(-1, 0, len(list_val)-1, list_val))

    def test_bin_search_middle(self):
        """check if search works for target in middle"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 5)

    def test_bin_search_left(self):
        """check if search works for target on left side"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3)

    def test_bin_search_right(self):
        """check if search works for target on right side"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 8)

if __name__ == "__main__":
        unittest.main()

    

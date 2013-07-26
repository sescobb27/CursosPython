import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_average_list(self):
    	"""
    	testing swaping the first 2 elements and 2 last elements of a average list
    	"""
    	nums = [1, 2, 3, 4, 5, 6]
    	swap_k(nums, 2)
    	self.assertEqual(nums,[5, 6, 3, 4, 1, 2])

    def test_swap_k_huge_list(self):
    	"""
    	testing swaping the first 5 elements and 5 last elements of a huge list
    	"""
    	nums = [1,3,5,7,9,20,30,12,34,4,1,35,2,4,5,6,13]
    	swap_k(nums, 5)
    	self.assertEqual(nums,[2, 4, 5, 6, 13, 20, 30, 12, 34, 4, 1, 35, 1, 3, 5, 7, 9])

    def test_swap_k_huge_list_swaping_the_middle(self):
    	"""
    	testing swaping the middle of the list (len(nums)//2)
    	"""
    	nums = [1,3,5,7,9,20,30,12,34,4,1,35,2,4,5,6,13]
    	size = len(nums)//2
    	swap_k(nums, size)
    	self.assertEqual(nums,[4, 1, 35, 2, 4, 5, 6, 13, 34, 1, 3, 5, 7, 9, 20, 30, 12])

    def test_swap_k_without_swaping(self):
    	"""
    	testing if a list without swaps to do in our method it's equal to the original
    	"""
    	nums = [1, 2, 3, 4, 5, 6]
    	swap_k(nums, 0)
    	self.assertEqual(nums,[1, 2, 3, 4, 5, 6])

    def test_swap_k_without_swaping_and_without_list(self):
    	"""
    	testing with an empty list and no swaps to do
    	"""
    	nums = []
    	swap_k(nums, 0)
    	self.assertEqual(nums,[])

if __name__ == '__main__':
    unittest.main(exit=False)

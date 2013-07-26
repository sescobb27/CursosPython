import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_large_list(self):
    	""" testing a large list containing stock price changes with possitives and negatives numbers """
    	actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    	expected = (0.14, -0.17)
    	self.assertEqual(actual,expected)

    def test_stock_price_summary_empty_list(self):
    	""" testing an empty list which return a tuple with 0 as values """
    	actual = a1.stock_price_summary([])
    	expected = (0,0)
    	self.assertEqual(actual,expected)

    def test_stock_price_summary_positive_list(self):
    	""" testing a large list containing possitive stock price changes """
    	actual = a1.stock_price_summary([10, 30, 20, 14, 30, 11, 2, 5])
    	expected = (122, 0)
    	self.assertEqual(actual,expected)

    def test_stock_price_summary_negative_list(self):
    	""" testing a large list containing negative stock price changes """
    	actual = a1.stock_price_summary([-10, -30, -20, -14, -30, -11, -2, -5])
    	expected = (0, -122)
    	self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)

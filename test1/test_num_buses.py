import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_above_maximum(self):
    	""" 
    		testing the minimum number of buses required to transport a number
    		of people above 50 (maximum number of people in one bus)
    	"""
    	actual = a1.num_buses(75)
    	expected = 2
    	self.assertEqual(actual,expected)

    def test_num_buses_under_maximum(self):
    	""" 
    		testing the minimum number of buses required to transport a number
    		of people under 50 (maximum number of people in one bus)
    	"""
    	actual = a1.num_buses(20)
    	expected = 1
    	self.assertEqual(actual,expected)

    def test_num_buses_equal_maximum(self):
    	""" 
    		testing the minimum number of buses required to transport a number
    		of people equal to 50 (maximum number of people in one bus)
    	"""
    	actual = a1.num_buses(50)
    	expected = 1
    	self.assertEqual(actual,expected)

    def test_num_buses_with_no_people(self):
        """ 
            testing the minimum number of buses required to transport 0 people
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main(exit=False)

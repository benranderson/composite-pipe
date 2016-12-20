import unittest
from inputs import Layup

class TestLayup(unittest.TestCase):
    """ Tests for inputs.Layup. """
    
    def test_Layup_omega(self):
        
        expected = 50
        actual = Layup(40,50,50,1).omega
        self.assertEqual(expected, actual, "Layup omega")
        
        
unittest.main()
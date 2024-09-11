from qr.qr import QRCode
import unittest

class TestModes(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode("012345")
    
    #TODO: test further edge cases for numeric/alphanumeric
    def test_is_numeric_one(self):
        self.assertEqual(self.qr1.is_numeric(), True)
        self.qr1.input = "abcdef"
        self.assertEqual(self.qr1.is_numeric(), False)
        self.qr1.input = "01234abc"
        self.assertEqual(self.qr1.is_numeric(), False)
        
    def test_is_alphanumeric_one(self):
        self.qr1.input = "DOPQA%"
        self.assertEqual(self.qr1.is_numeric(), False)
        self.assertEqual(self.qr1.is_alphanumeric(), True)
        
    def test_is_alphanumeric_two(self):
        self.qr1.input = " "
        self.assertEqual(self.qr1.is_alphanumeric(), True)
from qr.qr import QRCode
import unittest

class TestModes(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode("012345")
    
    #TODO: test further edge cases for numeric/alphanumeric
    def test_is_numeric_one(self):
        # test numeric
        self.assertEqual(self.qr1.is_numeric(), True)
        self.qr1.input = "abcdef"
        self.assertEqual(self.qr1.is_numeric(), False)
        self.qr1.input = "01234abc"
        self.assertEqual(self.qr1.is_numeric(), False)
        
    def test_is_alphanumeric_one(self):
        # test alphanumeric
        self.qr1.input = "DOPQA%"
        self.assertEqual(self.qr1.is_numeric(), False)
        self.assertEqual(self.qr1.is_alphanumeric(), True)
        
    def test_is_alphanumeric_two(self):
        # test for blank input
        self.qr1.input = " "
        self.assertEqual(self.qr1.is_alphanumeric(), True)
    
    def test_is_alphanumeric_three(self):
        # asserting that something that is numeric is also alphanumeric
        self.qr1.input = "012437"
        self.assertEqual(self.qr1.is_numeric(), True)
        self.assertEqual(self.qr1.is_alphanumeric(), True)
    
    def test_is_alphanumeric_four(self):
        self.qr1.input = "flame4$"
        self.assertEqual(self.qr1.is_alphanumeric(), False)
        
    def test_set_mode_one(self):
        self.qr1.set_mode()
        self.assertEqual(self.qr1.encoding_mode, 0b0001)
        
    def test_set_mode_two(self):
        self.qr1.input = "HELLO3"
        self.qr1.set_mode()
        self.assertEqual(self.qr1.encoding_mode, 0b0010)
        
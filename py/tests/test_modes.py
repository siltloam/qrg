from qr.qr import QRCode
import unittest

class TestModes(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode("012345")
    
    def test_is_numeric_one(self):
        self.assertEqual(self.qr1.is_numeric(), True)
        self.qr1.input = "abcdef"
        self.assertEqual(self.qr1.is_numeric(), False)
        self.qr1.input = "01234abc"
        self.assertEqual(self.qr1.is_numeric(), False)
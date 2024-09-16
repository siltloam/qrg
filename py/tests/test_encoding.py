import unittest
from qr.qr import QRCode

class TestEncoding(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode(None)
        
    def test_get_character_count_one(self):
        self.qr1.input = "012345"
        self.assertEqual(self.qr1.get_character_count(), bin(6))
        
    def test_get_character_count_two(self):
        self.qr1.input = "HELLO"
        self.assertEqual(self.qr1.get_character_count(), bin(5))
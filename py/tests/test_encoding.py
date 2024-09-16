import unittest
from qr.qr import QRCode

class TestEncoding(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode(None)
        
    def test_get_character_count_one(self):
        self.qr1.input = "012345"
        self.qr1.set_mode()
        self.assertEqual(self.qr1.get_character_count(), format(6, '010b'))
        
    def test_get_character_count_two(self):
        self.qr1.input = "HELLO"
        self.qr1.set_mode()
        self.assertEqual(self.qr1.get_character_count(), format(5, '09b'))
        
    def test_get_character_count_three(self):
        # testing for false input
        self.qr1.input = "♥"
        self.qr1.set_mode()
        self.assertEqual(self.qr1.encoding_mode, None)
        self.assertEqual(self.qr1.get_character_count(), None)
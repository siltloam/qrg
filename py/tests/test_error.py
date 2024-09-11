import unittest
from unittest.mock import patch
from qr.qr import QRCode


class TestError(unittest.TestCase):
    
    def setUp(self):
        self.qr1 = QRCode(None)
        
    def test_set_error_one(self):
        with patch('builtins.input', return_value='L'):
            self.qr1.set_error_correction_level()
        self.assertEqual(self.qr1.error_correction_level, 'L')
    
    def test_set_error_two(self):
        with patch('builtins.input', return_value='M'):
            self.qr1.set_error_correction_level()
        self.assertEqual(self.qr1.error_correction_level, 'M')
        
    def test_set_error_three(self):
        with patch('builtins.input', return_value='Q'):
            self.qr1.set_error_correction_level()
        self.assertEqual(self.qr1.error_correction_level, 'Q')
        
    def test_set_error_four(self):
        with patch('builtins.input', return_value='H'):
            self.qr1.set_error_correction_level()
        self.assertEqual(self.qr1.error_correction_level, 'H')
        
    def test_set_error_five(self):
        with patch('builtins.input', return_value='X'):
            self.qr1.set_error_correction_level()
        self.assertEqual(self.qr1.error_correction_level, None)
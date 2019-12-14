import unittest
import upper

class Testy_litery(unittest.TestCase):
    def test_upper(self):
        font = upper.duze('jakis teks z malymi literami')
        self.assertEqual(font, 'Jakis teks z malymi literami')
if __name__=='__main__':
    unittest.main()

import unittest
import upper

class Testy_litery(unittest.TestCase):
    def test_upper(self):
        font = upper.duze('jakis teks z malymi literami')
        self.assertEqual(font, 'Jakis Teks Z Malymi Literami')
if __name__=='__main__':
    unittest.main()

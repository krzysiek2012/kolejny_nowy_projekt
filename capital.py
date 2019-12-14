import unittest
import upper

class Testy_litery(unittest.TestCase):
    def test_upper(self):
        font = upper.duze('jakis teks z malymi literami')
        self.assertEqual(font, 'Jakis teks z malymi literami')

    def test_foldowanie(self):
        font=fold.male('Jakas Dziwna Powiastka O Niczym')
        self.assertEqual(font, jakas dziwna powiastka o niczym')
        


if __name__=='__main__':
    unittest.main()

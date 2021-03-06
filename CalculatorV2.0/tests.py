import unittest
from calculate_function import Scanner

class TestScanner(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Scanner('1+2').scann(), 3)

    def test_sub(self):
        self.assertEqual(Scanner('8-2').scann(), 6)

    def test_mul(self):
        self.assertEqual(Scanner('3*2').scann(), 6)

    def test_div(self):
        self.assertEqual(Scanner('10/2').scann(), 5)

    def test_expression(self):
        self.assertEqual(Scanner('10/2-3+22*2-(15+5)').scann(), 26)

    def test_expression2(self):
        self.assertEqual(Scanner('5+2*(5-3)').scann(), 9)

    def test_expression3(self):
        self.assertEqual(Scanner('5+2*(5-3)-1*5').scann(), 4)

    def test_expression4(self):
        self.assertEqual(Scanner('11/2').scann(), 5.5)

    def test_expression5(self):
        self.assertEqual(Scanner('(22+33)*2+(11+2)/2').scann(), 116.5)

if __name__ == '__main__':
    unittest.main()

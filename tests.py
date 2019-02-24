import unittest
import my_money

class TestAtm(unittest.TestCase):

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(10000), 10000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(1000), 10000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(5), 0)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(5000),12000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(-1), 5000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(100), 5000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(5000), 7000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(0), 11000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(10000), 500)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(13000), 500)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(-5000), 10000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(-1), 10000)

    def test_rise_money(self):
        self.assertEqual(my_money.money.rise_money(-13000), 10000)



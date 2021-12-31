import unittest
from Reservoir import Reservoir, Frequency


class ReservoirTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.name = "Test"
        self.category = "Home"

    def test_ctor(self):
        essential = True
        initial_value = 1234.56
        savings_rate = 50
        savings_rate_type = Frequency.MONTHLY
        limit = 200
        r = Reservoir(self.name, self.category, essential, initial_value, savings_rate, savings_rate_type, limit)
        self.assertEqual(r.name, self.name)
        self.assertEqual(r.category, self.category)
        self.assertEqual(r.essential, essential)
        self.assertEqual(r.value, initial_value)
        self.assertEqual(r.savings_rate, savings_rate)
        self.assertEqual(r.savings_rate_type, savings_rate_type)
        self.assertEqual(r.limit, limit)

    def test_set_value_lower_limit(self):
        r = Reservoir(self.name, self.category)
        self.assertRaises(IOError, r.set_value, -100)
        self.assertEqual(r.value, 0)


if __name__ == '__main__':
    unittest.main()

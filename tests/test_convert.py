import unittest

from tempconv.convert import c_to_f, c_to_k


class CelsiusToFahrenheitTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_f(0), 32)

    def test_boiling_point(self):
        self.assertAlmostEqual(c_to_f(100), 212)


class CelsiusToKelvinTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)


if __name__ == "__main__":
    unittest.main()

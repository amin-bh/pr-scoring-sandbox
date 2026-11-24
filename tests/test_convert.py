import unittest

from tempconv.convert import c_to_f, c_to_k, f_to_c


class CelsiusToFahrenheitTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_f(0), 32)

    def test_boiling_point(self):
        self.assertAlmostEqual(c_to_f(100), 212)


class CelsiusToKelvinTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)


class AbsoluteZeroTest(unittest.TestCase):
    def test_absolute_zero_itself_is_allowed(self):
        self.assertAlmostEqual(c_to_k(-273.15), 0)

    def test_below_absolute_zero_celsius_is_rejected(self):
        with self.assertRaises(ValueError):
            c_to_k(-300)

    def test_below_absolute_zero_fahrenheit_is_rejected(self):
        with self.assertRaises(ValueError):
            f_to_c(-500)


if __name__ == "__main__":
    unittest.main()

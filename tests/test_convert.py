import unittest

from tempconv.convert import c_to_f, c_to_k, f_to_c


class CelsiusToFahrenheitTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_f(0), 32)

    def test_boiling_point(self):
        self.assertAlmostEqual(c_to_f(100), 212)


class FahrenheitToCelsiusTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(f_to_c(32), 0)

    def test_boiling_point(self):
        self.assertAlmostEqual(f_to_c(212), 100)

    def test_round_trip(self):
        self.assertAlmostEqual(f_to_c(c_to_f(37)), 37)


class CelsiusToKelvinTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)


if __name__ == "__main__":
    unittest.main()

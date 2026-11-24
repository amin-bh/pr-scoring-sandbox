"""Temperature conversion helpers."""


def c_to_f(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32) * 9 / 5


def c_to_k(celsius):
    """Convert degrees Celsius to kelvin."""
    return celsius + 273.15

"""Temperature conversion helpers."""

ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def _require_physical(value, minimum, unit):
    """Raise ValueError if value is below absolute zero for the given unit."""
    if value < minimum:
        raise ValueError(f"{value} {unit} is below absolute zero ({minimum} {unit})")


def c_to_f(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    _require_physical(celsius, ABSOLUTE_ZERO_C, "C")
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Convert degrees Fahrenheit to degrees Celsius."""
    _require_physical(fahrenheit, ABSOLUTE_ZERO_F, "F")
    return (fahrenheit - 32) * 9 / 5


def c_to_k(celsius):
    """Convert degrees Celsius to kelvin."""
    _require_physical(celsius, ABSOLUTE_ZERO_C, "C")
    return celsius + 273.15

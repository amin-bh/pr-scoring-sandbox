"""Command-line entry point: python -m tempconv <value> <from> <to>."""
import argparse

from tempconv.convert import c_to_f, c_to_k, f_to_c

CONVERSIONS = {
    ("c", "f"): c_to_f,
    ("f", "c"): f_to_c,
    ("c", "k"): c_to_k,
}


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="tempconv", description="Convert temperatures betwen units."
    )
    parser.add_argument("value", type=float, help="the temperture to convert")
    parser.add_argument("source", choices=["c", "f"], help="unit to convert from")
    parser.add_argument("target", choices=["c", "f", "k"], help="unit to convert to")
    args = parser.parse_args(argv)

    func = CONVERSIONS.get((args.source, args.target))
    if func is None:
        parser.error(f"cannot convert {args.source} to {args.target}")
    try:
        result = func(args.value)
    except ValueError as err:
        parser.error(str(err))
    print(f"{result:.2f}")
    return 0

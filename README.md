# tempconv

A tiny command-line tool for converting temperatures between Celsius, Fahrenheit and Kelvin.

> This is a throwaway sandbox repository. It exists to hold sample pull requests
> used to test how pull requests are scored. The typos and bugs on `main` are
> deliberate.

## Installation

You only need Python 3.10 or newer. There are no dependencies.

```sh
git clone https://github.com/amin-bh/pr-scoring-sandbox.git
cd pr-scoring-sandbox
```

## Usage

```sh
python -m tempconv 100 c f    # 212.00
python -m tempconv 0 c k      # 273.15
```

The first argument is the value, the second the unit you convert from and the
third the unit you want to receive. Units are `c`, `f` and `k`, separate them
with a space.

## Running the tests

```sh
python -m unittest discover tests
```

## Docs

See [docs/README.md](docs/README.md).

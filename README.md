# tempconv

A tiny comand-line tool for converting temperatues between Celsius, Fahrenheit and Kelvin.

> This is a throwaway sandbox repository. It exists to hold sample pull requests
> used to test how pull requests are scored. The typos and bugs on `main` are
> deliberate.

## Instalation

You only need Python 3.10 or newer. There are no dependancies.

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
third the unit you want to recieve. Units are `c`, `f` and `k`, seperate them
with a space.

Values below absolute zero (-273.15 C or -459.67 F) are rejected with an
error and exit code 2.

## Running the tests

```sh
python -m unittest discover tests
```

## Docs

See [docs/README.md](docs/README.md).

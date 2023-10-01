# Random Recipes

[![pypi](https://img.shields.io/pypi/v/random-recipes)](https://pypi.org/project/random-recipes/#history)
[![downloads](https://img.shields.io/pypi/dm/random-recipes)](https://pypistats.org/packages/random-recipes)

Recipes to generate random instances of various types, beyond the scope of [random](https://docs.python.org/3/library/random.html).

Python's [random](https://docs.python.org/3/library/random.html) implements generators for pseudo-random bytes, integers, and sequences.
In [random-recipes](https://github.com/ipear3/random-recipes) we collect additional functions to generate random instances of common types that may be useful.

## Recipes

| Type                                                                                      | Function          |
|-------------------------------------------------------------------------------------------|-------------------|
| [bool](https://docs.python.org/3/library/stdtypes.html#boolean-values)                    | `random_bool`     |
| [bytes](https://docs.python.org/3/library/stdtypes.html?highlight=bytes#bytes-objects)    | `random_bytes`    |
| [decimal.Decimal](https://docs.python.org/3/library/decimal.html)                         | `random_decimal`  |
| [datetime.date](https://docs.python.org/3/library/datetime.html#date-objects)             | `random_date`     |
| [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)     | `random_datetime` |
| [float](https://docs.python.org/3/library/functions.html#float)                           | `random_float`    |
| [fractions.Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction) | `random_fraction` |
| [str](https://docs.python.org/3/library/stdtypes.html#str)                                | `random_str`      |

## Installation

Install the library with [pip](https://pip.pypa.io/en/stable/) from [PyPi](https://pypi.org/):
`pip install random-recipes`

---

## Development

`random-recipes` is developed by [@ipear3](https://github.com/ipear3).
This is a low-commitment project for practicing Python packaging, but it does try to contribute something of value.
Suggestions, comments, and contributions are welcome.

This project draws inspiration from [more-itertools](https://github.com/more-itertools/more-itertools), a well-designed, simple extension to a Python's [itertools](https://docs.python.org/3/library/itertools.html).


### Packaging & Dependency Management
Install the project with [Poetry](https://python-poetry.org/): `poetry install --with dev,test`

### Pre Commit
We'll use [pre-commit](https://pre-commit.com/) to ensure contributions maintain the development standards of the project, which follow.

### Standards

| Standard                                                                      | pre-commit   |
|-------------------------------------------------------------------------------|--------------|
| Code should be formatted by [Black](https://black.readthedocs.io/en/stable/). | black        |
| `pyproject.toml` should be kept up to-date.                                   | poetry-check |
| `poetry.lock` should be kept up-to-date.                                      | poetry-lock  |
| `pytest` should pass                                                          | pytest       |

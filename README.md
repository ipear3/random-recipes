# Random Recipes

[![pypi](https://img.shields.io/pypi/v/random-recipes)](https://pypi.org/project/random-recipes/#history)
[![downloads](https://img.shields.io/pypi/dm/random-recipes)](https://pypistats.org/packages/random-recipes)
![tests](images/badges/tests.svg)
![coverage](images/badges/coverage.svg)

Recipes to generate random instances of various types, beyond the scope of [random](https://docs.python.org/3/library/random.html).

Python's [random](https://docs.python.org/3/library/random.html) implements generators for pseudo-random bytes, integers, and sequences.
In [random-recipes](https://github.com/ipear3/random-recipes) we collect additional functions to generate random instances of common object types, collection types, and file types that may be useful.

## Recipes

### Objects
| Object Type                                                                               | Function          |
|-------------------------------------------------------------------------------------------|-------------------|
| [bool](https://docs.python.org/3/library/stdtypes.html#boolean-values)                    | `random_bool`     |
| [bytes](https://docs.python.org/3/library/stdtypes.html?highlight=bytes#bytes-objects)    | `random_bytes`    |
| [decimal.Decimal](https://docs.python.org/3/library/decimal.html)                         | `random_decimal`  |
| [datetime.date](https://docs.python.org/3/library/datetime.html#date-objects)             | `random_date`     |
| [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)     | `random_datetime` |
| [float](https://docs.python.org/3/library/functions.html#float)                           | `random_float`    |
| [fractions.Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction) | `random_fraction` |
| [int](https://docs.python.org/3/library/functions.html#int)                               | `random_int`      |
| [str](https://docs.python.org/3/library/stdtypes.html#str)                                | `random_str`      |

### Collections

| Collection Type                                                                                                   | Function       |
|-------------------------------------------------------------------------------------------------------------------|----------------|
| [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)                                        | `random_dict`  |
| [collections.abc.Iterable[dict]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable) | `random_dicts` |

### Files

| File Extension                                     | Function     |
|----------------------------------------------------|--------------|
| [.csv](https://docs.python.org/3/library/csv.html) | `random_csv` |


## Installation

Install the library with [pip](https://pip.pypa.io/en/stable/) from [PyPi](https://pypi.org/):
`pip install random-recipes`

---

## [Contributing](CONTRIBUTING.md)

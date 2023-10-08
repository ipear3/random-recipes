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

## Development

`random-recipes` is developed by [@ipear3](https://github.com/ipear3).
This is a low-commitment project for practicing Python packaging, but it does try to contribute something of value.
Suggestions, comments, and contributions are welcome.

This project draws inspiration from [more-itertools](https://github.com/more-itertools/more-itertools), a well-designed, simple extension to a Python's [itertools](https://docs.python.org/3/library/itertools.html).

### Packaging & Dependency Management
Get started with development by installing the project with `dev` and `test` dependency groups via [Poetry](https://python-poetry.org/): `poetry install --with dev`

### Formatting

We use [Black](https://black.readthedocs.io/en/stable/) to format our Python code.
We enforce black through a [pre-commit](https://pre-commit.com/) hook defined in [.pre-commit-config.yaml](.pre-commit-config.yaml).

### Testing

We use [pytest](https://github.com/pytest-dev/pytest) for testing, and our tests are located in [/tests](/tests).
We run our tests during the pre-push hook, `pytest`.

We use [coverage](https://github.com/nedbat/coveragepy) for test coverage, and we assert our test coverage is 95%.
Test coverage is checked during the pre-push hook, `coverage`.

### Documentation

We use [genbadge](https://smarie.github.io/python-genbadge/) to generate our `tests` and `coverage` [badges](/images/badges).
Badges are generated during the pre-push hooks `genbdage-tests` and `genbadge-coverage`.

### Releases, Tagging, and Versioning
Releases are automatically versioned by the poetry project's version in `pyproject.toml`.
Developers are responsible for incrementing the project version manually when they modify source code.
If they forget, the pre-push hook, `poetry-auto-semver` will increment the patch version by 1.

To create a release on [GitHub](https://github.com/ipear3/random-recipes/releases) and [PyPi](https://pypi.org/project/random-recipes/#history), push a commit to the `main` branch that affects any of the paths:
  - `random_recipes/**`
  - `pyproject.toml`
  - `poetry.lock`

The [release action](https://github.com/ipear3/random-recipes/actions/workflows/release.yml) will automatically:
1. Install the project
2. Test the project
3. Assert test coverage is 95%
4. Build the project for distribution
5. Create a GitHub release
   1. Autogenerate release notes
   2. Upload distribution files
6. Publish the project to PyPi

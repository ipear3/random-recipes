# Random Recipes

[![pypi](https://img.shields.io/pypi/v/random-recipes)](https://pypi.org/project/random-recipes/#history)
[![downloads](https://img.shields.io/pypi/dm/random-recipes)](https://pypistats.org/packages/random-recipes)
![tests](images/badges/tests.svg)
![coverage](images/badges/coverage.svg)

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
Get started with development by installing the project with `dev` and `test` dependency groups via [Poetry](https://python-poetry.org/): `poetry install --with dev`

### Formatting

We format our python code according to [Black](https://black.readthedocs.io/en/stable/).
We enforce black through a [pre-commit](https://pre-commit.com/) hook defined in [.pre-commit-config.yaml](.pre-commit-config.yaml).

### Testing

We use [pytest](https://github.com/pytest-dev/pytest) for testing, and our tests are located in [/tests](/tests).
We run our full test suite pre-commit and in the action [on-push](https://github.com/ipear3/random-recipes/actions/workflows/on-push.yml) defined in [.github/workflows/on-push.yml](.github/workflows/on-push.yml).

We use [coverage](https://github.com/nedbat/coveragepy) for test coverage, and we assert our test coverage is 100%.
Test coverage is checked pre-commit and in the action [on-push](https://github.com/ipear3/random-recipes/actions/workflows/on-push.yml).

### Documentation
Badges are generated and stored [in the repo](/images/badges) pre-commit by [genbadge](https://smarie.github.io/python-genbadge/).
- ![tests](images/badges/tests.svg)
- ![coverage](images/badges/coverage.svg)

### Releases, Tagging, and Versioning
To create a release on [GitHub](https://github.com/ipear3/random-recipes/releases) and [PyPi](https://pypi.org/project/random-recipes/#history), tag a commit like `*.*.*` and merge it to the `main` branch.

Release tagged commits pushed to the `main` branch trigger the [release action](https://github.com/ipear3/random-recipes/actions/workflows/release.yml) defined in [release.yml](https://github.com/ipear3/random-recipes/blob/main/.github/workflows/release.yml).

We use the [dynamic versioning plugin for Poetry](https://github.com/mtkennerly/poetry-dynamic-versioning) to populate the project version from our release tag during `poetry build` or `poetry publish`.
This means we delegate responsibility to enforce tag uniqueness to `git`, and tag pattern matching to GitHub Actions.
This is a nice balance - our workflow is to make one tag, and it propagates where we need it to.

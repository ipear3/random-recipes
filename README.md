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

### Testing

Although tests are automatically run pre-commit, developers must agree to create robust tests.

### Releases
Releases are triggered automatically by commits to branch `main` with a tag like `*.*.*`, thanks to the [Release action](https://github.com/ipear3/random-recipes/actions/workflows/release.yml).
The release action is defined in [release.yml](https://github.com/ipear3/random-recipes/blob/main/.github/workflows/release.yml).

#### Tags

Commits are automatically tagged like `*.*.*` any time a new project version in [pyproject.toml](pyproject.toml) is committed, thanks to the `git-tag` pre-commit hook.
The tag pre-commit hook is defined in [.pre-commit-config.yaml](.pre-commit-config.yaml).

### Standards

Project standards are enforced by [pre-commit](https://pre-commit.com/) hooks and [GitHub Actions](https://docs.github.com/en/actions).

| Standard                                                                      | Script                              | Pre-commit Hook                                                                                                      | GitHub Action                                                                     |
|-------------------------------------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Source changes should bump the project version.                               | `poetry version patch/minor/major`  |                                                                                                                      |                                                                                   |
| `README.md` should display badges for `tests`, `coverage`.                    | `scripts/tests-and-coverage.sh`     |                                                                                                                      |                                                                                   |
| Code should be formatted by [Black](https://black.readthedocs.io/en/stable/). | `black .`                           | [black](https://black.readthedocs.io/en/stable/integrations/source_version_control.html#version-control-integration) |                                                                                   |
| Source changes should pass `pytest`.                                          |                                     | `pytest`                                                                                                             |                                                                                   |
| Test coverage percentage should be 100%.                                      |                                     | `coverage`                                                                                                           |                                                                                   |
| `pyproject.toml` should be kept up to-date.                                   |                                     | [poetry-check](https://python-poetry.org/docs/master/pre-commit-hooks/#poetry-check)                                 |                                                                                   |
| `poetry.lock` should be kept up-to-date.                                      |                                     | [poetry-lock](https://python-poetry.org/docs/master/pre-commit-hooks/#poetry-check)                                  |                                                                                   |
| Source changes should be tagged.                                              | `git tag $(poetry version --short)` |                                                                                                                      |                                                                                   |
| Source changes should be released.                                            |                                     |                                                                                                                      | [Release](https://github.com/ipear3/random-recipes/actions/workflows/release.yml) |

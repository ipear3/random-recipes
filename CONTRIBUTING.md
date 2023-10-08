# Contributing

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

## Releases, Tagging, Versioning, and Publishing
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

"""Recipes to generate random instances of various types, beyond the scope of random."""
import collections.abc
import logging
import string
from datetime import date, datetime
from decimal import Decimal
import random
import fractions


def random_bool() -> bool:
    """Return a random :class:`bool`."""
    return random.choice((False, True))


def random_bytes(n: int = 1) -> bytes:
    """Generate n random :class:`bytes`. Alias of `random.randbytes`."""
    return random.randbytes(n=n)


def random_decimal(scale: int = 40, precision: int = None) -> Decimal:
    """Return a random :class:`Decimal` number `precision` digits in length.

    Arguments:
        precision: Total digits
        scale: Digits right of the decimal point.
    """
    if precision is None:
        precision = scale
    if precision < scale:
        logging.warning(
            f"Given precision {precision} is less than {scale}. Resulting Decimal will be {precision} digits."
        )
        scale = precision
    int_digits = random_str(string.digits, k=precision - scale)
    first_decimal_digits = random_str(string.digits, k=scale - 1)
    last_decimal_digit = random.randint(1, 9)
    return Decimal(f"{int_digits}.{first_decimal_digits}{last_decimal_digit}")


def random_date(_min: date = date.min, _max: date = date.max) -> date:
    """Return a random :class:`date` between `_min` and `_max`."""
    return _min + random.random() * (_max - _min)


def random_datetime(
    _min: datetime = datetime.min,
    _max: datetime = datetime.max,
) -> datetime:
    """Return a random :class:`datetime` between `_min` and `_max`."""
    return _min + random.random() * (_max - _min)


def random_float(float_digits: int = 40, int_min: int = 0, int_max: int = 0) -> float:
    """Return a random :class:`float` number `k` digits in length.

    Each digit is a random digit, 0-9, except the last digit, which is random 1-9.
    """
    return random.randint(int_min, int_max) + float(
        random_str(string.digits, k=float_digits)
    )


def random_fraction(
    num_min: int = 0, num_max: int = 1, den_min: int = 1, den_max: int = 2
) -> fractions.Fraction:
    """Return a random :class:`fractions.Fraction`."""
    return fractions.Fraction(
        random.randint(num_min, num_max), random.randint(den_min, den_max)
    )


def random_str(
    characters: collections.abc.Sequence = string.printable,
    relative_weights: collections.abc.Sequence[float | fractions.Fraction] = None,
    cumulative_weights: collections.abc.Sequence[float | fractions.Fraction] = None,
    k: int = 1,
) -> str:
    """Return a random :class:`str` with `k` `characters` chosen.

    Nearly an alias of `random.choices()` - elements are chosen from characters with replacement.

    If the relative weights or cumulative weights are not specified, the selections are made with equal probability.
    """
    return "".join(
        random.choices(
            population=characters,
            weights=relative_weights,
            cum_weights=cumulative_weights,
            k=k,  # Example change to attempt auto-tag on change to source code.
        )
    )

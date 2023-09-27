"""Recipes to generate random instances of various types, beyond the scope of random."""
from datetime import date, datetime
from decimal import Decimal
import random
from string import digits


def random_decimal(whole_digits: int = 1, decimal_digits: int = 40):
    """Return a random :class:`Decimal` number `k` digits in length.

    Each digit is a random digit, 0-9, except the last digit, which cannot be 0."""
    whole_str = "".join(str(d) for d in random.choices(digits, k=whole_digits))
    decimal_str = "".join(str(d) for d in random.choices(digits, k=decimal_digits))
    return Decimal(f"{whole_str}.{decimal_str}")


def random_date(
    _min: date = date.min, _max: date = date.max
):
    """Return a random :class:`date` between _min and _max."""
    return _min + random.random() * (_max - _min)


def random_datetime(
    _min: datetime = datetime.min,
    _max: datetime = datetime.max,
):
    """Return a random :class:`datetime` between _min and _max."""
    return _min + random.random() * (_max - _min)

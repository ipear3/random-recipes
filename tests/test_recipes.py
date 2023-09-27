from random_recipes import Decimal, date, datetime, random_decimal, random_date, random_datetime


def test_random_decimal_is_decimal():
    """Assert that `random_decimal()` returns an instance of :class:`Decimal`"""
    assert isinstance(random_decimal(), Decimal)


def test_random_date_is_date():
    """Assert that `random_date()` returns an instance of :class:`date`"""
    assert isinstance(random_date(), date)


def test_random_datetime_is_datetime():
    """Assert that `random_datetime()` returns an instance of :class:`datetime`"""
    assert isinstance(random_datetime(), datetime)


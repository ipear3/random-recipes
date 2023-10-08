from random_recipes.objects import *


class TestRandomBool:
    def test_random_bool_is_bool(self):
        assert isinstance(random_bool(), bool)


class TestRandomBytes:
    def test_random_bytes_is_bytes(self):
        assert isinstance(random_bytes(), bytes)


class TestRandomDecimal:
    def test_random_decimal_is_decimal(self):
        assert isinstance(random_decimal(), Decimal)

    def test_random_decimal_is_less_than_1_if_precision_eq_scale(self):
        assert random_decimal(scale=2, precision=2) < 1

    def test_random_decimal_is_given_scale(self):
        scale = 3
        assert len(str(random_decimal(scale=scale)).split(".")[1]) == scale

    def test_random_decimal_is_given_precision(self):
        precision = 3
        decimal_str = str(random_decimal(precision=precision))
        assert (
            len(decimal_str) == precision + 1 + 1 if decimal_str.startswith("0") else 0
        )


class TestRandomDate:
    def test_random_date_is_date(self):
        assert isinstance(random_date(), date)


class TestRandomDatetime:
    def test_random_datetime_is_datetime(self):
        assert isinstance(random_datetime(), datetime)


class TestRandomFloat:
    def test_random_float_is_float(self):
        assert isinstance(random_float(), float)


class TestRandomFraction:
    def test_random_fraction_is_fraction(self):
        assert isinstance(random_fraction(), fractions.Fraction)


class TestRandomStr:
    def test_random_str_is_str(self):
        assert isinstance(random_str(), str)

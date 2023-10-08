from random_recipes.collections import *


class TestRandomDict:
    def test_random_dict_is_dict(self):
        assert isinstance(random_dict(), dict)


class TestRandomDicts:
    def test_random_dicts_is_dicts(self):
        assert isinstance(random_dicts(), collections.abc.Iterable)

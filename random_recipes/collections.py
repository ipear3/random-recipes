from random_recipes.objects import *


def random_dict(types: list[SupportedRandomObjects] = supported_random_objects):
    """Return a random :class:`dict` containing `types` as keys and random object instances as values."""
    d = {}
    for t in types:
        if t in object_names_to_random_function_map:
            d[t] = object_names_to_random_function_map[t]()
    return d


def random_dicts(
    n: int = 10, id_start: int = 0, id_label: str = "id", **random_dict_kwargs
):
    """Yield random :class:`dict` instances except for the `id_label` key, which will be autoincremented from `id_start`"""
    for i in range(id_start, id_start + n):
        r = {id_label: i}
        d = random_dict(**random_dict_kwargs)
        if id_label in d:
            logging.warning(
                f"Was given an id_label, {id_label} that will be overridden by `random_dict(**random_dict_kwargs)`"
            )
        r.update(**d)
        yield r

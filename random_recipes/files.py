import csv
from pathlib import Path

from random_recipes.collections import *


def random_csv(
    file="data/random.csv",
    header: bool = True,
    n: int = 100,
    id_start: int = 1,
    id_label: str = "id",
):
    """Generate random :class:`dict` instances and write them to a csv."""
    path = Path(file)
    dicts = random_dicts(n=n, id_start=id_start, id_label=id_label)
    with open(path, "w", newline="") as text_io:
        for i, record in enumerate(dicts):
            if i == 0:
                writer = csv.DictWriter(
                    text_io, fieldnames=record.keys(), dialect="unix"
                )
                if header:
                    writer.writeheader()
            writer.writerow(record)
    return path

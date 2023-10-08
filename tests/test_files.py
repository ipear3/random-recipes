from random_recipes.files import *


class TestRandomCSV:
    def test_random_csv_is_csv(self):
        file = Path("data/random.csv")
        file.parent.mkdir(exist_ok=True, parents=True)
        file = random_csv(file=file)
        with open(file, newline="") as file:
            reader = csv.reader(file, dialect="unix")
            for row in reader:
                print(row)
            ok = True
        assert ok

coverage run --data-file reports/.coverage -m pytest --junitxml=reports/tests.xml;
genbadge tests -i reports/tests.xml -o images/badges/tests.svg;
coverage xml --data-file reports/.coverage -o reports/coverage.xml --fail-under 100;
genbadge coverage -i reports/coverage.xml -o images/badges/coverage.svg;

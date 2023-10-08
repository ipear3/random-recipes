#!/usr/bin/env sh
# Pytest via Coverage -> Tests badge
echo "Running pytest via coverage..." &&
coverage run --data-file reports/.coverage -m pytest --junitxml=reports/tests.xml &&
echo "Running genbadge tests..." &&
genbadge tests -i reports/tests.xml -o images/badges/tests.svg;
# Coverage -> Coverage badge
echo "Running coverage..." &&
coverage xml --data-file reports/.coverage -o reports/coverage.xml --fail-under 95;
echo "Running genbadge coverage..."
genbadge coverage -i reports/coverage.xml -o images/badges/coverage.svg;

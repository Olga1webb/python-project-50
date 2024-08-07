install:
	poetry install
gendiff:
	poetry run gendiff -h
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 hexlet_code
report:
	./gradlew jacocoTestReport
test:
	poetry run pytest

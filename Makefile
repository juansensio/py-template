pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist

clean:
	rm -rf dist
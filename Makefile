pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist

clean:
	rm -rf dist

docum: 
	python setup.py build_sphinx --build-dir doc/build
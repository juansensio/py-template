pypi: test docum dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist

clean:
	rm -rf dist

docum: 
	python setup.py build_sphinx --build-dir doc/build
	rm -rf docs
	mv doc/build/html docs

test:
	python -m unittest discover -s tests -p '*_test.py'
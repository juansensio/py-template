
pypi: test docum dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist

clean:
	rm -rf dist

docum: 
	python tools/rst.py kk sphinx/source
	python setup.py build_sphinx --build-dir sphinx/build
	rm -rf docs
	mv sphinx/build/html docs

test:
	python -m unittest discover -s tests -p '*_test.py'

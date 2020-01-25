# run this script to start a new project

import os
import sys
from shutil import copyfile


def save(name, text):
    # save some text in a file
    text_file = open(name, "w")
    text_file.write(text)
    text_file.close()


name = sys.argv[1]

# create a folder with the name of the library
os.mkdir(name)

# copy template
copyfile('tools/templates/template.py', f'{name}/template.py')
copyfile('tools/templates/__init__.py', f'{name}/__init__.py')

# create a folder for the tests
os.mkdir('tests')
copyfile('tools/templates/example_test.py', 'tests/example_test.py')

# set up github actions
os.mkdir('.github')
os.mkdir('.github/workflows')
copyfile('tools/templates/main.yml', '.github/workflows/main.yml')

# create some required folders for testing
os.mkdir('sphinx/build')
os.mkdir('sphinx/source/.templates')
os.mkdir('sphinx/source/.static')

# create a Makefile with all the tools
makefile = f"""
pypi: test docum dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist

clean:
	rm -rf dist

docum: 
	python tools/rst.py {name} sphinx/source
	python setup.py build_sphinx --build-dir sphinx/build
	rm -rf docs
	mv sphinx/build/html docs

test:
	python -m unittest discover -s tests -p '*_test.py'
"""
save('Makefile', makefile)

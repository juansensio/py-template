
from sphinx.setup_command import BuildDoc
from packaging.version import parse
import setuptools
assert parse(setuptools.__version__) >= parse('36.2')
cmdclass = {'build_sphinx': BuildDoc}

name = 'your-project-name-here'
version = '0.0'
release = '0.0.0'
author = 'The Author'
description = 'your description here'
email = 'theauthor@gmail.com'
url = 'https://github.com/theauthor/repo-name'
keywords = ['some', 'keywords', 'here']

setuptools.setup(
    name=name,
    packages=setuptools.find_packages(),
    version=release,
    license='MIT',
    description=description,
    author=author,
    author_email=email,
    url=url,
    keywords=keywords,
    # install_requires=[
    #    'numpy',
    #    'pandas',
    # ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'sphinx/source')}}
)

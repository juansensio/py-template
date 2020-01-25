
from packaging.version import parse
import setuptools
assert parse(setuptools.__version__) >= parse('36.2')

setuptools.setup(
    name='mylibtemplate',         # How you named your package folder (MyLib)
    packages=['mylibtemplate'],   # Chose the same as "name"
    version='0.0.3',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='python template',
    author='Juan Sensio',                  # Type in your name
    author_email='juansensio03@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/juansensio/py-template',
    # I explain this later on
    # download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['python', 'template'],
    # install_requires=[            # I get to this in a second
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
)

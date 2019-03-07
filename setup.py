from setuptools import find_packages, setup


# Package meta-data.
NAME = 'deck-crafter'
DESCRIPTION = "A web app for building decks and managing card collections for CCGs."
URL = 'https://github.com/jbradberry/deck-crafter'
EMAIL = 'jeff.bradberry@gmail.com'
AUTHOR = 'Jeff Bradberry'
# REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = [
    'Django', 'psycopg2', 'Pillow',
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description="",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    package_dir={'starsweb': 'starsweb'},
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Games/Entertainment',
    ],
)

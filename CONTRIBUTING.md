# Contributing

## Getting Started

Fork this repository, clone it to your local machine, and once ready, open a PR for any maintainer(s) to review and merge. Please email brandon.donelan@outlook.com if you have any inquiries not mentioned or covered in this documentation.

## Development Install

Please note OS and Python environment details when contributing to assure we can narrow down potential enviornment-related issues.

```sh
$ python -V # windows
$ python -m venv env
```

Install the necessary dependencies.

```sh
$ pip install -e ".[dev]"
```

## Upload to PyPI

```sh
$ python -m pip install --user --upgrade setuptools wheel
$ python -m pip install --user --upgrade twine
$ python setup.py sdist bdist_wheel
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/ezodbc-x.x.x.tar.gz
$ twine upload dist/*
```
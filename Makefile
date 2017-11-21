.PHONY: default build

default:
	@echo "no default action"

build:
	# python setup.py sdist bdist_wheel
	# using workaround for this issue:
	# https://bitbucket.org/pypa/wheel/issues/99/cannot-exclude-directory
	python setup.py sdist
	pip wheel --verbose --no-index --no-deps --wheel-dir dist dist/*.tar.gz

all: dist

dist:
	python setup.py sdist

install:
	pip install --upgrade .

clean:
	rm -vrf \
		vpc_free.egg-info \
		build \
		dist

.PHONY: all dist install clean

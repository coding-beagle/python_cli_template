clean:
	{ \
		make clean-venv ;\
		make clean-build ;\
	}


clean-venv:
	rm -rf .venv

clean-build:
	rm -rf dist

venv:
	python -m venv .venv

build:
	python setup.py sdist bdist_wheel

install:
	{ \
		. .venv/scripts/activate ;\
		pip install -e . ;\
	}
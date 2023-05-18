install:
	pip install --upgrade pip -r requirements.txt

install-dev:
	pip install --upgrade pip -r requirements.dev.txt

test:
	pytest -svv .

debugtest:
	PYTHONBREAKPOINT=ipdb.set_trace pytest -svv .
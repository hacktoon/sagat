test:
	pytest -svv .

debugtest:
	PYTHONBREAKPOINT=ipdb.set_trace pytest -svv .
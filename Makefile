clean: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


lint: ## check style with pylint
	pylint composite

test:
	py.test

coverage:
	py.test --cov-report term --cov-report html --cov=composite tests
run:
	uvicorn app.main:app --reload
format:
	python -m pip install ruff && ruff format .
lint:
	python -m pip install ruff && ruff check --fix .
test:
	pytest -q

setup:
	@poetry install

run:
	@poetry run streamlit run src/app.py

fmt:
	@poetry run black .

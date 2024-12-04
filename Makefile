# Makefile
SHELL = /bin/bash

format:
	isort backend
	black backend

tests:
	pytest

data:
	python -c "from backend.app.comet_predictor.generator import create_wish_list_data_files; create_wish_list_data_files()"

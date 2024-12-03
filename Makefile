# Makefile
SHELL = /bin/bash

format:
	isort backend
	black backend

tests:
	pytest
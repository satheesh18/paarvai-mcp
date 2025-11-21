.PHONY: help install dev-install test lint format clean build publish

help:
	@echo "Paarvai MCP Server - Development Commands"
	@echo ""
	@echo "install        Install package"
	@echo "dev-install    Install package with dev dependencies"
	@echo "test           Run tests"
	@echo "lint           Run linting checks"
	@echo "format         Format code"
	@echo "clean          Clean build artifacts"
	@echo "build          Build package"
	@echo "publish        Publish to PyPI"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src/ tests/
	mypy src/

format:
	black src/ tests/
	ruff check --fix src/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	python -m twine upload dist/*

publish-test: build
	python -m twine upload --repository testpypi dist/*

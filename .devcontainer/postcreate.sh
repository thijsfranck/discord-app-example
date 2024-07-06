#!/bin/bash

# Install dependencies
poetry install

# Mark the git repository as safe
git config --global --add safe.directory $PWD

# Install pre-commit hooks
poetry run pre-commit install

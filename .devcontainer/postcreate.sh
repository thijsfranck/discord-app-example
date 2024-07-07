#!/bin/bash

# Mark the git repository as safe
git config --global --add safe.directory $PWD

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install

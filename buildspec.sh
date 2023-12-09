#!/bin/bash

# Execute the commands defined in each phase of the buildspec.yml manually in your terminal.
# This shell script to automate the manual steps.


# Stop on first error
set -e

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -r requirements-dev.txt

# Pre-build commands
echo "Running pre-build steps..."

# Build commands
echo "Running pytest..."
pytest tests/

echo "Building Sphinx documentation..."
sphinx-apidoc -o docs/source py_docs_example
sphinx-build -v -b html -c docs docs docs/build

# psot build
echo Build completed on `date`

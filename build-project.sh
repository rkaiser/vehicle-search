#!/usr/bin/env bash

# Fail the script if failures occur during the script
set -euo pipefail

PACKAGE_NAME="vehicle-search"
# Specify the target environment's python version
PYTHON_VERSION="3.13"

rm -rf dist wheelhouse "${PACKAGE_NAME}-offline-bundle.tar.gz"
mkdir wheelhouse

uv lock

uv export \
  --format requirements.txt \
  --no-dev \
  --no-emit-project \
  --output-file wheelhouse/requirements.txt

uv build --wheel --out-dir wheelhouse

uv run --with pip python -m pip download \
  -r wheelhouse/requirements.txt \
  --platform manylinux2014_x86_64 \
  --python-version "$PYTHON_VERSION" \
  --only-binary=:all: \
  -d wheelhouse

tar -czf "${PACKAGE_NAME}-offline-bundle.tar.gz" wheelhouse install-project.sh install-system.sh uninstall-system.sh

echo "Created ${PACKAGE_NAME}-offline-bundle.tar.gz"
#!/usr/bin/env bash

# Fail the script if failures occur during the script
set -euo pipefail

PACKAGE_NAME="vehicle-search"
VENV_DIR=".venv"
FORCE=false

if [[ "${1:-}" == "--force" ]]; then
  FORCE=true
fi

if [[ -d "$VENV_DIR" ]]; then
  if [[ "$FORCE" == true ]]; then
    echo "Removing existing $VENV_DIR..."
    rm -rf "$VENV_DIR"
  else
    echo "Error: $VENV_DIR already exists."
    echo "Remove it manually or rerun with:"
    echo "  ./install.sh --force"
    exit 1
  fi
fi

python -m venv "$VENV_DIR"

source "$VENV_DIR/bin/activate"

python -m pip install \
  --no-index \
  --find-links ./wheelhouse \
  "$PACKAGE_NAME"

"$PACKAGE_NAME" --help

echo
echo "Installed successfully."
echo "Activate with:"
echo "  source $VENV_DIR/bin/activate"
#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME="vehicle-search"
COMMAND_NAME="vehicle-search"

INSTALL_DIR="/opt/$PACKAGE_NAME"
BIN_DIR="/usr/local/bin"
FORCE=false

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WHEELHOUSE="$SCRIPT_DIR/wheelhouse"

if [[ "${1:-}" == "--force" ]]; then
  FORCE=true
fi

if [[ "$(id -u)" -ne 0 ]]; then
  echo "This system-wide installer must be run as root."
  echo "Try:"
  echo "  sudo ./install-system.sh"
  exit 1
fi

if [[ -d "$INSTALL_DIR" ]]; then
  if [[ "$FORCE" == true ]]; then
    echo "Removing existing $INSTALL_DIR..."
    rm -rf "$INSTALL_DIR"
  else
    echo "Error: $INSTALL_DIR already exists."
    echo "Remove it manually or rerun with:"
    echo "  sudo ./install-system.sh --force"
    exit 1
  fi
fi

mkdir -p "$INSTALL_DIR"

python -m venv "$INSTALL_DIR/.venv"

"$INSTALL_DIR/.venv/bin/python" -m pip install \
  --no-index \
  --find-links "$WHEELHOUSE" \
  "$PACKAGE_NAME"

ln -sf "$INSTALL_DIR/.venv/bin/$COMMAND_NAME" "$BIN_DIR/$COMMAND_NAME"

chmod -R a+rX "$INSTALL_DIR"

echo
echo "Installed successfully."
echo "Command available at:"
echo "  $BIN_DIR/$COMMAND_NAME"
echo
echo "Try:"
echo "  $COMMAND_NAME --help"
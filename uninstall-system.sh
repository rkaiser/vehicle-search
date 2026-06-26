#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME="vehicle-search"
COMMAND_NAME="vehicle-search"

INSTALL_DIR="/opt/$PACKAGE_NAME"
BIN_LINK="/usr/local/bin/$COMMAND_NAME"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "This uninstaller must be run as root."
  echo "Try:"
  echo "  sudo ./uninstall-system.sh"
  exit 1
fi

echo "Removing command link..."
rm -f "$BIN_LINK"

echo "Removing install directory..."
rm -rf "$INSTALL_DIR"

echo "Uninstalled $PACKAGE_NAME."
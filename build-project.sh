#!/usr/bin/env bash

set -euo pipefail

PACKAGE_NAME="vehicle-search"

./build-wheelhouse.sh

tar -czf "${PACKAGE_NAME}-offline-bundle.tar.gz" wheelhouse install-project.sh install-system.sh uninstall-system.sh data config.toml

echo "Created ${PACKAGE_NAME}-offline-bundle.tar.gz"
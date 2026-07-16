#!/usr/bin/env bash

set -euo pipefail

# Build the project wheel and download all dependencies.
# Ideally, this mode creates wheelhouse/ but does not create the old tar.gz.
./build-wheelhouse.sh

# Build the Debian binary package.
dpkg-buildpackage \
    --build=binary \
    --unsigned-source \
    --unsigned-changes
To get started

These steps leverage the use of uv to manage the python environment, project dependencies, etc. Other tools can be used (i.e. hatch) or handled manually, but the use of uv simplifies many of the steps one may want to take when building a project.

Install uv using the instructions for  your environment provided by https://docs.astral.sh/uv/getting-started/installation/

Lint

To leverage the linting rules within VS code, install the vs code RUFF extension published by Astral software.


Installation Steps

tar -xzf my-offline-bundle.tar.gz
python -m venv .venv
source .venv/bin/activate
python -m pip install --no-index --find-links ./wheelhouse vehicle-search


To get started

These steps leverage the use of uv to manage the python environment, project dependencies, etc. Other tools can be used (i.e. hatch) or handled manually, but the use of uv simplifies many of the steps one may want to take when building a project.

Install uv using the instructions for  your environment provided by https://docs.astral.sh/uv/getting-started/installation/

Lint

To leverage the linting rules within VS code, install the vs code RUFF extension published by Astral software.

### Build Steps
The build relies on the tool `uv` and is expected to be executed using a linux distribution. If running on windows, the recommendation is to use WSL2 with one of the commong linux distributions.

Edit the `./build-project.sh` to ensure that the proper python version is defined for the target system.

Once the edited properly, execute the command `./build-project.sh`. 

This will execute the necessary build commands and produce a `.tar.gz` which will be used to install on the target machine.


### Installation Steps

Copy the `.tar.gz` file that was produced during the build steps and extract it to the installation location on the target machine.
```bash
tar -xvf project-offline-bundle.tar.gz
```
One of the files in the extracted bundle is the `install-project.sh` file. This file should be executed in the installation location.

```bash
./install-project.sh
```





## Basic Project Setup
### To get started

These steps leverage the use of `uv` to manage the python environment, project dependencies, etc. Other tools can be used (i.e. hatch) or handled manually, but the use of `uv` simplifies many of the steps one may want to take when building a project.

In order to install follow the instructions for  your environment provided by https://docs.astral.sh/uv/getting-started/installation/

Once installed, `uv` can be used to manage and install multiple versions of python as well as to manage and install project dependencies.

### Lint

#### Ruff
The de-facto standard for enforcing python coding and formatting standards is the linting tool called ruff. Ruff can be added to the project as a development dependency using the following `uv` command:

```bash
uv add --dev ruff
```

To leverage the Ruff linting rules within VS code, install the vs code Ruff extension published by Astral software.

#### Type Hints
Since Python is not a statically typed languaged, a developer can encounter type problems if proper care is not taken. To encourage consideration of proper data types, python has included the ability to provide `type hints` when defining variables, arguments, etc. Since the language uses dynamic typing, the type hints will not prohibit incorrect types from being used; however, by using type hints the developer can employ tools to check that the used types match the expected types. The developers of `uv` have a created a tool called `ty` which can be used to check that types are being defined and are being used as expected. The tool `ty` can be added using the following:

```bash
uv add --dev ty
```

Once added the tool can be used to check that appropriate typing is used by using the following command:
```bash
uv run ty check
```

To integrate `ty` type checking within VS code, install the ty extension published by Astral software.
To ensure that `ty` works properly with pylance, you may need to update the `.vscode/settings.json` like the following:
```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "off",

  "ty.disableLanguageServices": true,
  "ty.diagnosticMode": "workspace",
  "ty.showSyntaxErrors": false,

  "ruff.enable": true
}
```

### Development Scripts
To support many of the common develpment tasks, this project leverages the capabilities of `uv` along with `poethepoet` and has been configured via `pyproject.toml`. Within the `pyproject.toml` file there are a number of scripts that can be used to help the develpment process. These scripts can be used to execute project, run tests, determine test coverage statistices, and lint the project according to industry standard rules. Some of the key scripts can be executed as follows:

```bash
# run the application
uv run vehicle-search find --make=honda --year=2015 --config=./config.toml
uv run vehicle-search find-sales --make=honda --model=accord --year=2015 --config=./config.toml
# run the unit tests using pytest
uv run poe test
# run the coverage statistics using pytest-cov
uv run poe cov
# run the linter using 
uv run poe lint
```

### Build Steps
The build process also leverages `uv` and is expected to be executed using a linux distribution. If running on windows, the recommendation is to use WSL2 with one of the common linux distributions.

Edit the `./build-project.sh` to ensure that the proper python version is defined for the target system.

Once the edited properly, execute the command `./build-project.sh`. 

This will execute the necessary build commands and produce a `.tar.gz` which will be used to install on the target machine.

### Installation Steps
The assumption is that the target system will already have python installed at the version that is defined in `build-project.sh` script. If the target machine does not include python, adjustments will need to be made to the build and installation steps.

Copy the `.tar.gz` file that was produced during the build steps and extract it to the installation location on the target machine.
```bash
tar -xvf project-offline-bundle.tar.gz
```
The files in the extracted bundle include `install-project.sh` and `install-system.sh`. These files can be used to install the packaged. To install the file local to the shell that the user is using, the `install-project.sh` can be used. This will make it such that the package is only accessible to the user performing installation. To make the package globally available, the `install-system.sh` script can be used. This will need to be executed as root as it is installed in the `/opt` folder.

```bash
# Install locally for the logged in user
./install-project.sh
```
or 
```bash
# Install globally to the system
sudo ./install-system.sh
```

Additionally, the project includes an `uninstall-system.sh` script which can be used to remove the project from the system. This will also need to be executed as root.

```bash
sudo ./uninstall-system.sh
```

### Running the Application
Once the application is installed it can be executed by executing the application entry point, which is defined as `PACKAGE_NAME` in the the `install-project.sh` or `COMMAND_NAME` in the `install-system.sh`.

```bash
# Command to find models for specific make and year
vehicle-search find --make=honda --year=2015 --config=./config.toml

# command find find sales for the specific make, model, and year
vehicle-search find-sales --make=honda --model=accord --year=2015 --config=./config.toml
```

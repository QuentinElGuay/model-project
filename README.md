# model-project
Does nothing but try to make it well.

## Introduction
This project is about implanting good practices for project management (like: tests, packaging, versionning, CI/CD, etc.) and serves as a model for future projects.

## Minimal requirements
This project requires:
- python >= 3.10.0
- pip >= v21.1 because it doesn't offer a setup.py file.

## Installation
To install locally the project and its dependencies, run:
```bash
pip install -e .
```

## Develop for the project
### Installation
To install the test libraries and different development tools, install the dev package:
```bash
pip install -e .[dev]
```

### Tests
To run the unit tests, run:
```bash
pytest
```

### Before commiting
This project uses the  tool to format the 
Please format your Python files to pre-defined standards using [blue](https://pypi.org/project/blue/), before committing, using:
```bash
blue .
```
> **Warning**
> This operation might modify your Python files and require you to reload them.

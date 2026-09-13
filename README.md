<span align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![tests](https://github.com/billwallis/github-manager/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/github-manager/actions/workflows/tests.yaml)
[![coverage](https://raw.githubusercontent.com/billwallis/github-manager/refs/heads/main/coverage.svg)](https://smarie.github.io/python-genbadge/)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/github-manager/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/github-manager/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/github-manager)](https://shields.io/badges/git-hub-last-commit)

</span>

---

# GitHub Manager

CLI for managing GitHub repositories.

## Contributing

Install the dependencies:

```shell
pip install --editable . --group dev --group test
pre-commit install --install-hooks
```

## Usage

```shell
ghm org <org-name>
ghm repo <org-name>/<repo-name>
```

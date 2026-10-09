from __future__ import annotations

import argparse
import importlib.metadata
from collections.abc import Sequence

from github_manager import reports

SUCCESS = 0
FAILURE = 1


def _get_version() -> str:
    return f"%(prog)s {importlib.metadata.version('github-manager')}"


def _org(args: argparse.Namespace) -> int:
    """
    Generate a report for the given GitHub organisation.
    """

    try:
        reports.org(args.login)
        return SUCCESS
    except Exception as e:
        print(f"error: {e}")
        return FAILURE


def _user(args: argparse.Namespace) -> int:
    """
    Generate a report for the given GitHub user.
    """

    try:
        reports.user(args.login)
        return SUCCESS
    except Exception as e:
        print(f"error: {e}")
        return FAILURE


def _repo(args: argparse.Namespace) -> int:
    """
    Generate a report for the given GitHub repository.
    """

    try:
        reports.repo(args.repository_name)
        return SUCCESS
    except Exception as e:
        print(f"error: {e}")
        return FAILURE


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=_get_version(),
    )
    subparsers = parser.add_subparsers(dest="command")

    parser__org = subparsers.add_parser("org")
    parser__org.add_argument("login")

    parser__user = subparsers.add_parser("user")
    parser__user.add_argument("login")

    parser__repo = subparsers.add_parser("repo")
    parser__repo.add_argument("repository_name")

    args = parser.parse_args(argv)
    if args.command == "org":
        return _org(args)
    if args.command == "user":
        return _user(args)
    if args.command == "repo":
        return _repo(args)

    parser.print_help()
    return SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover

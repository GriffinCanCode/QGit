"""QGits - Quick Git operations automation tool.

This package provides automation and convenience functions for common Git operations.
"""

__version__ = "1.1.5"

"""QGit package initialization."""

from qgits.cli import main as cli_main
from qgits.qgit import main
from qgits.qgit_author import (
    AuthorCommand,
    show_author,
)
from qgits.qgit_author_data import (
    get_random_advice,
    get_random_facts,
    get_random_quote,
)


__all__ = [
    "AuthorCommand",
    "cli_main",
    "get_random_advice",
    "get_random_facts",
    "get_random_quote",
    "main",
    "show_author",
]

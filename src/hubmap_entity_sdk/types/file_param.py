# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileParam"]


class FileParam(TypedDict, total=False):
    description: str
    """A description of the file.

    The Dataset.thumbnail_file does not have this file description.
    """

    file_uuid: str
    """The HuBMAP unique identifier for the file."""

    filename: str
    """The name of the file."""

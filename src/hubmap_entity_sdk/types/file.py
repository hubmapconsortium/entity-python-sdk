# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    description: Optional[str] = None
    """A description of the file.

    The Dataset.thumbnail_file does not have this file description.
    """

    file_uuid: Optional[str] = None
    """The HuBMAP unique identifier for the file."""

    filename: Optional[str] = None
    """The name of the file."""

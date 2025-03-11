# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Person"]


class Person(BaseModel):
    affiliation: Optional[str] = None
    """The institution that the person is affiliated with."""

    first_name: Optional[str] = None
    """The full name of the person."""

    last_name: Optional[str] = None
    """The last name of the person."""

    middle_name_or_initial: Optional[str] = None
    """The middle name or initial of the person."""

    orcid_id: Optional[str] = None
    """The ORCID iD of the person."""

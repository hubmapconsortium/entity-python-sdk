# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PersonParam"]


class PersonParam(TypedDict, total=False):
    affiliation: str
    """The institution that the person is affiliated with."""

    first_name: str
    """The full name of the person."""

    last_name: str
    """The last name of the person."""

    middle_name_or_initial: str
    """The middle name or initial of the person."""

    orcid_id: str
    """The ORCID iD of the person."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .person_param import PersonParam

__all__ = ["CollectionParam"]


class CollectionParam(TypedDict, total=False):
    contacts: Iterable[PersonParam]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contributors: Iterable[PersonParam]
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    title: str
    """The title of the Collection"""

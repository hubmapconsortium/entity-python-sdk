# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

from .person_param import PersonParam
from .donor_metadata_param import DonorMetadataParam

__all__ = ["DonorParam", "Metadata"]


class Metadata(TypedDict, total=False):
    living_donor_data: Iterable[DonorMetadataParam]
    """Information about the donor who's tissue was used.

    The tissue was obtained during a procedure. Only living_donor_data or
    organ_donor_data, not both can be defined for a single donor.
    """

    organ_donor_data: Iterable[DonorMetadataParam]
    """Information about the donor who's organ(s) was/were used.

    The organ was obtained via an organ donation program from a deceaced donor. Only
    living_donor_data or organ_donor_data, not both can be defined for a single
    donor.
    """


class DonorParam(TypedDict, total=False):
    contacts: Iterable[PersonParam]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    creators: Iterable[PersonParam]
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    description: str
    """Free text description of the donor"""

    group_uuid: str
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    image_files_to_add: List[str]
    """List of temporary file ids with an optional description.

    Provide as a json array with an temp_file_id and description attribute for each
    element like {"files":
    [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
    one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}
    """

    image_files_to_remove: List[str]
    """List of image files previously uploaded to delete.

    Provide as a json array of the file_uuids of the file like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    lab_donor_id: str
    """A lab specific identifier for the donor."""

    label: str
    """Lab provided, de-identified name for the donor"""

    metadata: Metadata
    """Donor metadata as an array of UMLS codes and descriptions"""

    protocol_url: str
    """
    The protocols.io doi url pointing the protocol describing the donor selection,
    inclusion/exclusion criteria
    """

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

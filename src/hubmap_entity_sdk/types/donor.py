# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .file import File
from .person import Person
from .._models import BaseModel
from .donor_metadata import DonorMetadata

__all__ = ["Donor", "Metadata"]


class Metadata(BaseModel):
    living_donor_data: Optional[List[DonorMetadata]] = None
    """Information about the donor who's tissue was used.

    The tissue was obtained during a procedure. Only living_donor_data or
    organ_donor_data, not both can be defined for a single donor.
    """

    organ_donor_data: Optional[List[DonorMetadata]] = None
    """Information about the donor who's organ(s) was/were used.

    The organ was obtained via an organ donation program from a deceaced donor. Only
    living_donor_data or organ_donor_data, not both can be defined for a single
    donor.
    """


class Donor(BaseModel):
    contacts: Optional[List[Person]] = None
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    created_by_user_displayname: Optional[str] = None
    """The name of the person or process authenticated when creating the object"""

    created_by_user_email: Optional[str] = None
    """
    The email address of the person or process authenticated when creating the
    object.
    """

    created_by_user_sub: Optional[str] = None
    """
    The subject id as provided by the authorization mechanism for the person or
    process authenticated when creating the object.
    """

    created_timestamp: Optional[int] = None
    """The timestamp of when the node was created.

    The format is an integer representing milliseconds since midnight Jan 1, 1970
    """

    creators: Optional[List[Person]] = None
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    data_access_level: Optional[Literal["consortium", "public"]] = None
    """One of the values: public, consortium"""

    description: Optional[str] = None
    """Free text description of the donor"""

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

    entity_type: Optional[Literal["Donor"]] = None
    """Entity type constant"""

    group_name: Optional[str] = None
    """
    The displayname of globus group which the user who created this entity is a
    member of
    """

    group_uuid: Optional[str] = None
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    hubmap_id: Optional[str] = None
    """
    A HuBMAP Consortium wide unique identifier randomly generated in the format
    HBM###.ABCD.### for every entity.
    """

    image_files: Optional[List[File]] = None
    """List of uploaded image files and descriptions of the files.

    Stored in db as a stringfied json array.
    """

    lab_donor_id: Optional[str] = None
    """A lab specific identifier for the donor."""

    label: Optional[str] = None
    """Lab provided, de-identified name for the donor"""

    last_modified_timestamp: Optional[int] = None
    """The timestamp of when the object was last modified.

    The format is an integer representing milliseconds since midnight, Jan 1, 1970
    """

    last_modified_user_displayname: Optional[str] = None
    """
    The name of the person or process which authenticated when the object was last
    modified.
    """

    last_modified_user_email: Optional[str] = None
    """
    The email address of the person or process which authenticated when the object
    was last modified.
    """

    last_modified_user_sub: Optional[str] = None
    """
    The subject id of the user who last modified the entity as provided by the
    authorization mechanism for the person or process authenticated when the object
    was modified.
    """

    metadata: Optional[Metadata] = None
    """Donor metadata as an array of UMLS codes and descriptions"""

    protocol_url: Optional[str] = None
    """
    The protocols.io doi url pointing the protocol describing the donor selection,
    inclusion/exclusion criteria
    """

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    submission_id: Optional[str] = None
    """The hubmap internal id with embedded semantic information e.g.: VAN0003.

    This id is generated at creation time which tracks the lab, donor, organ and
    sample hierarchy per the following:
    https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing
    """

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """

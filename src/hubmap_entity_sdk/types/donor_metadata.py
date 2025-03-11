# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DonorMetadata"]


class DonorMetadata(BaseModel):
    code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS source vocabulary terms.
    """

    concept_id: Optional[str] = None
    """This is the Concept ID from the HuBMAP Knowledge Graph.

    Currently limited to UMLS concepts.
    """

    data_type: Optional[Literal["Nominal", "Numeric"]] = None
    """This is the data type of thw record.

    Numeric types will generally have non-null data_value. Nominal types will
    generally have null data_value.
    """

    data_value: Optional[str] = None
    """The data value of the record."""

    end_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the end of this event (this is to construct time series records of clinical data
    for event-level data not donor-level data). An epty of zero value designates
    missing data or that this field is not applicable for the concept
    """

    graph_version: Optional[str] = None
    """
    This is the version of the HuBMAP Knowledge Graph that the Concept appears in,
    currently the version of UMLS that is used.
    """

    grouping_code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS vocabulary codes. This code corresponds to the grouping_concept.
    """

    grouping_concept: Optional[str] = None
    """
    This is the Concept ID from the HuBMAP Knowledge Graph, currently limited to
    UMLS concetps, that is to be used for grouping the record.
    """

    grouping_concept_preferred_term: Optional[str] = None
    """
    This is the preferred display term for the facet in which this record should be
    counted for faceted search in the portal. It may or may not correspond to a term
    in UMLS for the grouping concept.
    """

    grouping_sab: Optional[str] = None
    """
    This is a grouping for the source vocabulary in the HuBMAP Knowledge Graph,
    currently limited to UMLS source vocabularies.. This sab corresponds to the
    grouping_code.
    """

    numeric_operator: Optional[Literal["EQ", "GT", "LT"]] = None
    """
    This is the numeric operator for the data value .This enables inputing
    thresholds and ranges for data values by using greater than or less than.
    """

    preferred_term: Optional[str] = None
    """This is the preferred display term for the item.

    It may or may not correspond to a term in UMLS for this concept.
    """

    sab: Optional[str] = None
    """This is the source vocabulary in the HuBMAP Knowledge Graph.

    Currently limited to UMLS source vocabularies.
    """

    start_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the start of this event (this is to construct time series records of clinical
    data for event-level data not donor-level data). An empty or zero value
    designates missing data or that this field is not applicable for the concept.
    """

    units: Optional[str] = None
    """This are the units for the data value."""

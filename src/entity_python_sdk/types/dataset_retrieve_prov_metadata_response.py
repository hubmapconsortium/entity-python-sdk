# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .donor import Donor
from .sample import Sample
from .dataset import Dataset

__all__ = ["DatasetRetrieveProvMetadataResponse"]


class DatasetRetrieveProvMetadataResponse(Dataset):
    donors: Optional[List[Donor]] = None
    """List of Donors for the dataset"""

    organs: Optional[List[Sample]] = None
    """List of Samples of sub-type organ for the dataset"""

    samples: Optional[List[Sample]] = None
    """List of Samples not of sub-type organ for the dataset"""

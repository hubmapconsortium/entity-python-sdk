# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DatasetListRevisionsParams"]


class DatasetListRevisionsParams(TypedDict, total=False):
    include_dataset: Literal["true", "false"]
    """A case insensitive string.

    Any value besides true will have no effect. If the string is 'true', the full
    dataset for each revision will be included in the response
    """

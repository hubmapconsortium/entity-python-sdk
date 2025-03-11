# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.entity_type_list_response import EntityTypeListResponse

__all__ = ["EntityTypesResource", "AsyncEntityTypesResource"]


class EntityTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-sdk-python#with_streaming_response
        """
        return EntityTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityTypeListResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeListResponse,
        )


class AsyncEntityTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-sdk-python#with_streaming_response
        """
        return AsyncEntityTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityTypeListResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return await self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeListResponse,
        )


class EntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = to_raw_response_wrapper(
            entity_types.list,
        )


class AsyncEntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = async_to_raw_response_wrapper(
            entity_types.list,
        )


class EntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = to_streamed_response_wrapper(
            entity_types.list,
        )


class AsyncEntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = async_to_streamed_response_wrapper(
            entity_types.list,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sample_retrieve_prov_info_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sample_retrieve_prov_info_response import SampleRetrieveProvInfoResponse

__all__ = ["SamplesResource", "AsyncSamplesResource"]


class SamplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hubmap-api-devs/entity-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hubmap-api-devs/entity-python-sdk#with_streaming_response
        """
        return SamplesResourceWithStreamingResponse(self)

    def retrieve_prov_info(
        self,
        *,
        group_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SampleRetrieveProvInfoResponse:
        """
        returns all provenance information for a each sample in a json format

        Args:
          group_uuid: The uuid of the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/samples/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"group_uuid": group_uuid}, sample_retrieve_prov_info_params.SampleRetrieveProvInfoParams
                ),
            ),
            cast_to=SampleRetrieveProvInfoResponse,
        )


class AsyncSamplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hubmap-api-devs/entity-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hubmap-api-devs/entity-python-sdk#with_streaming_response
        """
        return AsyncSamplesResourceWithStreamingResponse(self)

    async def retrieve_prov_info(
        self,
        *,
        group_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SampleRetrieveProvInfoResponse:
        """
        returns all provenance information for a each sample in a json format

        Args:
          group_uuid: The uuid of the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/samples/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"group_uuid": group_uuid}, sample_retrieve_prov_info_params.SampleRetrieveProvInfoParams
                ),
            ),
            cast_to=SampleRetrieveProvInfoResponse,
        )


class SamplesResourceWithRawResponse:
    def __init__(self, samples: SamplesResource) -> None:
        self._samples = samples

        self.retrieve_prov_info = to_raw_response_wrapper(
            samples.retrieve_prov_info,
        )


class AsyncSamplesResourceWithRawResponse:
    def __init__(self, samples: AsyncSamplesResource) -> None:
        self._samples = samples

        self.retrieve_prov_info = async_to_raw_response_wrapper(
            samples.retrieve_prov_info,
        )


class SamplesResourceWithStreamingResponse:
    def __init__(self, samples: SamplesResource) -> None:
        self._samples = samples

        self.retrieve_prov_info = to_streamed_response_wrapper(
            samples.retrieve_prov_info,
        )


class AsyncSamplesResourceWithStreamingResponse:
    def __init__(self, samples: AsyncSamplesResource) -> None:
        self._samples = samples

        self.retrieve_prov_info = async_to_streamed_response_wrapper(
            samples.retrieve_prov_info,
        )

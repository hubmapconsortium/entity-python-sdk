# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from entity_python_sdk import EntityPythonSDK, AsyncEntityPythonSDK
from entity_python_sdk.types import SampleRetrieveProvInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSamples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_prov_info(self, client: EntityPythonSDK) -> None:
        sample = client.samples.retrieve_prov_info()
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_prov_info_with_all_params(self, client: EntityPythonSDK) -> None:
        sample = client.samples.retrieve_prov_info(
            group_uuid="group_uuid",
        )
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_prov_info(self, client: EntityPythonSDK) -> None:
        response = client.samples.with_raw_response.retrieve_prov_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sample = response.parse()
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_prov_info(self, client: EntityPythonSDK) -> None:
        with client.samples.with_streaming_response.retrieve_prov_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sample = response.parse()
            assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSamples:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_prov_info(self, async_client: AsyncEntityPythonSDK) -> None:
        sample = await async_client.samples.retrieve_prov_info()
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_prov_info_with_all_params(self, async_client: AsyncEntityPythonSDK) -> None:
        sample = await async_client.samples.retrieve_prov_info(
            group_uuid="group_uuid",
        )
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_prov_info(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.samples.with_raw_response.retrieve_prov_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sample = await response.parse()
        assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_prov_info(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.samples.with_streaming_response.retrieve_prov_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sample = await response.parse()
            assert_matches_type(SampleRetrieveProvInfoResponse, sample, path=["response"])

        assert cast(Any, response.is_closed) is True

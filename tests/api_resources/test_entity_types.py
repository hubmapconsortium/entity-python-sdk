# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity_sdk import HubmapEntitySDK, AsyncHubmapEntitySDK
from hubmap_entity_sdk.types import EntityTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntityTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: HubmapEntitySDK) -> None:
        entity_type = client.entity_types.list()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: HubmapEntitySDK) -> None:
        response = client.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: HubmapEntitySDK) -> None:
        with client.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntityTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncHubmapEntitySDK) -> None:
        entity_type = await async_client.entity_types.list()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubmapEntitySDK) -> None:
        response = await async_client.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubmapEntitySDK) -> None:
        async with async_client.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

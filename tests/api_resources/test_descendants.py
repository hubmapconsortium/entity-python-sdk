# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity_sdk import HubmapEntitySDK, AsyncHubmapEntitySDK
from hubmap_entity_sdk.types import DescendantRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDescendants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: HubmapEntitySDK) -> None:
        descendant = client.descendants.retrieve(
            "id",
        )
        assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: HubmapEntitySDK) -> None:
        response = client.descendants.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        descendant = response.parse()
        assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: HubmapEntitySDK) -> None:
        with client.descendants.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            descendant = response.parse()
            assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: HubmapEntitySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.descendants.with_raw_response.retrieve(
                "",
            )


class TestAsyncDescendants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubmapEntitySDK) -> None:
        descendant = await async_client.descendants.retrieve(
            "id",
        )
        assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubmapEntitySDK) -> None:
        response = await async_client.descendants.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        descendant = await response.parse()
        assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubmapEntitySDK) -> None:
        async with async_client.descendants.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            descendant = await response.parse()
            assert_matches_type(DescendantRetrieveResponse, descendant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubmapEntitySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.descendants.with_raw_response.retrieve(
                "",
            )

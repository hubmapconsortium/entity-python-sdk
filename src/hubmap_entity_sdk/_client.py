# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import doi, parents, uploads, children, datasets, entities, ancestors, descendants, entity_types_all
    from .resources.doi import DoiResource, AsyncDoiResource
    from .resources.parents import ParentsResource, AsyncParentsResource
    from .resources.uploads import UploadsResource, AsyncUploadsResource
    from .resources.children import ChildrenResource, AsyncChildrenResource
    from .resources.datasets import DatasetsResource, AsyncDatasetsResource
    from .resources.ancestors import AncestorsResource, AsyncAncestorsResource
    from .resources.descendants import DescendantsResource, AsyncDescendantsResource
    from .resources.entity_types_all import EntityTypesAllResource, AsyncEntityTypesAllResource
    from .resources.entities.entities import EntitiesResource, AsyncEntitiesResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HubmapEntitySDK",
    "AsyncHubmapEntitySDK",
    "Client",
    "AsyncClient",
]


class HubmapEntitySDK(SyncAPIClient):
    # client options
    bearer_token: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous HubmapEntitySDK client instance.

        This automatically infers the `bearer_token` argument from the `HUBMAP_ENTITY_SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("HUBMAP_ENTITY_SDK_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("HUBMAP_ENTITY_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://entity.api.hubmapconsortium.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def entity_types_all(self) -> EntityTypesAllResource:
        from .resources.entity_types_all import EntityTypesAllResource

        return EntityTypesAllResource(self)

    @cached_property
    def ancestors(self) -> AncestorsResource:
        from .resources.ancestors import AncestorsResource

        return AncestorsResource(self)

    @cached_property
    def descendants(self) -> DescendantsResource:
        from .resources.descendants import DescendantsResource

        return DescendantsResource(self)

    @cached_property
    def parents(self) -> ParentsResource:
        from .resources.parents import ParentsResource

        return ParentsResource(self)

    @cached_property
    def children(self) -> ChildrenResource:
        from .resources.children import ChildrenResource

        return ChildrenResource(self)

    @cached_property
    def doi(self) -> DoiResource:
        from .resources.doi import DoiResource

        return DoiResource(self)

    @cached_property
    def datasets(self) -> DatasetsResource:
        from .resources.datasets import DatasetsResource

        return DatasetsResource(self)

    @cached_property
    def uploads(self) -> UploadsResource:
        from .resources.uploads import UploadsResource

        return UploadsResource(self)

    @cached_property
    def with_raw_response(self) -> HubmapEntitySDKWithRawResponse:
        return HubmapEntitySDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubmapEntitySDKWithStreamedResponse:
        return HubmapEntitySDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHubmapEntitySDK(AsyncAPIClient):
    # client options
    bearer_token: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHubmapEntitySDK client instance.

        This automatically infers the `bearer_token` argument from the `HUBMAP_ENTITY_SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("HUBMAP_ENTITY_SDK_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("HUBMAP_ENTITY_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://entity.api.hubmapconsortium.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def entity_types_all(self) -> AsyncEntityTypesAllResource:
        from .resources.entity_types_all import AsyncEntityTypesAllResource

        return AsyncEntityTypesAllResource(self)

    @cached_property
    def ancestors(self) -> AsyncAncestorsResource:
        from .resources.ancestors import AsyncAncestorsResource

        return AsyncAncestorsResource(self)

    @cached_property
    def descendants(self) -> AsyncDescendantsResource:
        from .resources.descendants import AsyncDescendantsResource

        return AsyncDescendantsResource(self)

    @cached_property
    def parents(self) -> AsyncParentsResource:
        from .resources.parents import AsyncParentsResource

        return AsyncParentsResource(self)

    @cached_property
    def children(self) -> AsyncChildrenResource:
        from .resources.children import AsyncChildrenResource

        return AsyncChildrenResource(self)

    @cached_property
    def doi(self) -> AsyncDoiResource:
        from .resources.doi import AsyncDoiResource

        return AsyncDoiResource(self)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        from .resources.datasets import AsyncDatasetsResource

        return AsyncDatasetsResource(self)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        from .resources.uploads import AsyncUploadsResource

        return AsyncUploadsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHubmapEntitySDKWithRawResponse:
        return AsyncHubmapEntitySDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubmapEntitySDKWithStreamedResponse:
        return AsyncHubmapEntitySDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HubmapEntitySDKWithRawResponse:
    _client: HubmapEntitySDK

    def __init__(self, client: HubmapEntitySDK) -> None:
        self._client = client

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def entity_types_all(self) -> entity_types_all.EntityTypesAllResourceWithRawResponse:
        from .resources.entity_types_all import EntityTypesAllResourceWithRawResponse

        return EntityTypesAllResourceWithRawResponse(self._client.entity_types_all)

    @cached_property
    def ancestors(self) -> ancestors.AncestorsResourceWithRawResponse:
        from .resources.ancestors import AncestorsResourceWithRawResponse

        return AncestorsResourceWithRawResponse(self._client.ancestors)

    @cached_property
    def descendants(self) -> descendants.DescendantsResourceWithRawResponse:
        from .resources.descendants import DescendantsResourceWithRawResponse

        return DescendantsResourceWithRawResponse(self._client.descendants)

    @cached_property
    def parents(self) -> parents.ParentsResourceWithRawResponse:
        from .resources.parents import ParentsResourceWithRawResponse

        return ParentsResourceWithRawResponse(self._client.parents)

    @cached_property
    def children(self) -> children.ChildrenResourceWithRawResponse:
        from .resources.children import ChildrenResourceWithRawResponse

        return ChildrenResourceWithRawResponse(self._client.children)

    @cached_property
    def doi(self) -> doi.DoiResourceWithRawResponse:
        from .resources.doi import DoiResourceWithRawResponse

        return DoiResourceWithRawResponse(self._client.doi)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithRawResponse:
        from .resources.datasets import DatasetsResourceWithRawResponse

        return DatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithRawResponse:
        from .resources.uploads import UploadsResourceWithRawResponse

        return UploadsResourceWithRawResponse(self._client.uploads)


class AsyncHubmapEntitySDKWithRawResponse:
    _client: AsyncHubmapEntitySDK

    def __init__(self, client: AsyncHubmapEntitySDK) -> None:
        self._client = client

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def entity_types_all(self) -> entity_types_all.AsyncEntityTypesAllResourceWithRawResponse:
        from .resources.entity_types_all import AsyncEntityTypesAllResourceWithRawResponse

        return AsyncEntityTypesAllResourceWithRawResponse(self._client.entity_types_all)

    @cached_property
    def ancestors(self) -> ancestors.AsyncAncestorsResourceWithRawResponse:
        from .resources.ancestors import AsyncAncestorsResourceWithRawResponse

        return AsyncAncestorsResourceWithRawResponse(self._client.ancestors)

    @cached_property
    def descendants(self) -> descendants.AsyncDescendantsResourceWithRawResponse:
        from .resources.descendants import AsyncDescendantsResourceWithRawResponse

        return AsyncDescendantsResourceWithRawResponse(self._client.descendants)

    @cached_property
    def parents(self) -> parents.AsyncParentsResourceWithRawResponse:
        from .resources.parents import AsyncParentsResourceWithRawResponse

        return AsyncParentsResourceWithRawResponse(self._client.parents)

    @cached_property
    def children(self) -> children.AsyncChildrenResourceWithRawResponse:
        from .resources.children import AsyncChildrenResourceWithRawResponse

        return AsyncChildrenResourceWithRawResponse(self._client.children)

    @cached_property
    def doi(self) -> doi.AsyncDoiResourceWithRawResponse:
        from .resources.doi import AsyncDoiResourceWithRawResponse

        return AsyncDoiResourceWithRawResponse(self._client.doi)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithRawResponse:
        from .resources.datasets import AsyncDatasetsResourceWithRawResponse

        return AsyncDatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithRawResponse:
        from .resources.uploads import AsyncUploadsResourceWithRawResponse

        return AsyncUploadsResourceWithRawResponse(self._client.uploads)


class HubmapEntitySDKWithStreamedResponse:
    _client: HubmapEntitySDK

    def __init__(self, client: HubmapEntitySDK) -> None:
        self._client = client

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def entity_types_all(self) -> entity_types_all.EntityTypesAllResourceWithStreamingResponse:
        from .resources.entity_types_all import EntityTypesAllResourceWithStreamingResponse

        return EntityTypesAllResourceWithStreamingResponse(self._client.entity_types_all)

    @cached_property
    def ancestors(self) -> ancestors.AncestorsResourceWithStreamingResponse:
        from .resources.ancestors import AncestorsResourceWithStreamingResponse

        return AncestorsResourceWithStreamingResponse(self._client.ancestors)

    @cached_property
    def descendants(self) -> descendants.DescendantsResourceWithStreamingResponse:
        from .resources.descendants import DescendantsResourceWithStreamingResponse

        return DescendantsResourceWithStreamingResponse(self._client.descendants)

    @cached_property
    def parents(self) -> parents.ParentsResourceWithStreamingResponse:
        from .resources.parents import ParentsResourceWithStreamingResponse

        return ParentsResourceWithStreamingResponse(self._client.parents)

    @cached_property
    def children(self) -> children.ChildrenResourceWithStreamingResponse:
        from .resources.children import ChildrenResourceWithStreamingResponse

        return ChildrenResourceWithStreamingResponse(self._client.children)

    @cached_property
    def doi(self) -> doi.DoiResourceWithStreamingResponse:
        from .resources.doi import DoiResourceWithStreamingResponse

        return DoiResourceWithStreamingResponse(self._client.doi)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithStreamingResponse:
        from .resources.datasets import DatasetsResourceWithStreamingResponse

        return DatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithStreamingResponse:
        from .resources.uploads import UploadsResourceWithStreamingResponse

        return UploadsResourceWithStreamingResponse(self._client.uploads)


class AsyncHubmapEntitySDKWithStreamedResponse:
    _client: AsyncHubmapEntitySDK

    def __init__(self, client: AsyncHubmapEntitySDK) -> None:
        self._client = client

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def entity_types_all(self) -> entity_types_all.AsyncEntityTypesAllResourceWithStreamingResponse:
        from .resources.entity_types_all import AsyncEntityTypesAllResourceWithStreamingResponse

        return AsyncEntityTypesAllResourceWithStreamingResponse(self._client.entity_types_all)

    @cached_property
    def ancestors(self) -> ancestors.AsyncAncestorsResourceWithStreamingResponse:
        from .resources.ancestors import AsyncAncestorsResourceWithStreamingResponse

        return AsyncAncestorsResourceWithStreamingResponse(self._client.ancestors)

    @cached_property
    def descendants(self) -> descendants.AsyncDescendantsResourceWithStreamingResponse:
        from .resources.descendants import AsyncDescendantsResourceWithStreamingResponse

        return AsyncDescendantsResourceWithStreamingResponse(self._client.descendants)

    @cached_property
    def parents(self) -> parents.AsyncParentsResourceWithStreamingResponse:
        from .resources.parents import AsyncParentsResourceWithStreamingResponse

        return AsyncParentsResourceWithStreamingResponse(self._client.parents)

    @cached_property
    def children(self) -> children.AsyncChildrenResourceWithStreamingResponse:
        from .resources.children import AsyncChildrenResourceWithStreamingResponse

        return AsyncChildrenResourceWithStreamingResponse(self._client.children)

    @cached_property
    def doi(self) -> doi.AsyncDoiResourceWithStreamingResponse:
        from .resources.doi import AsyncDoiResourceWithStreamingResponse

        return AsyncDoiResourceWithStreamingResponse(self._client.doi)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithStreamingResponse:
        from .resources.datasets import AsyncDatasetsResourceWithStreamingResponse

        return AsyncDatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithStreamingResponse:
        from .resources.uploads import AsyncUploadsResourceWithStreamingResponse

        return AsyncUploadsResourceWithStreamingResponse(self._client.uploads)


Client = HubmapEntitySDK

AsyncClient = AsyncHubmapEntitySDK

# Entities

Types:

```python
from entity_python_sdk.types import (
    Collection,
    Donor,
    DonorMetadata,
    Entity,
    Epicollection,
    Instanceof,
    Publication,
    Sample,
    Upload,
    EntityCreateResponse,
    EntityUpdateResponse,
    EntityCreateMultipleSamplesResponse,
    EntityGetGlobusURLResponse,
    EntityListAncestorOrgansResponse,
    EntityListCollectionsResponse,
    EntityListEntityTypesResponse,
    EntityListSiblingsResponse,
    EntityListTupletsResponse,
    EntityListUploadsResponse,
)
```

Methods:

- <code title="post /entities/new/{entity_type}">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">create</a>(entity_type, \*\*<a href="src/entity_python_sdk/types/entity_create_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_create_response.py">EntityCreateResponse</a></code>
- <code title="put /entities/{id}">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">update</a>(id, \*\*<a href="src/entity_python_sdk/types/entity_update_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_update_response.py">EntityUpdateResponse</a></code>
- <code title="post /entities/multiple-samples/{count}">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">create_multiple_samples</a>(count) -> <a href="./src/entity_python_sdk/types/entity_create_multiple_samples_response.py">EntityCreateMultipleSamplesResponse</a></code>
- <code title="get /entities/{id}/globus-url">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">get_globus_url</a>(id) -> str</code>
- <code title="get /entities/{id}/instanceof/{type}">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">is_instance_of</a>(type, \*, id) -> <a href="./src/entity_python_sdk/types/instanceof.py">Instanceof</a></code>
- <code title="get /entities/{id}/ancestor-organs">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_ancestor_organs</a>(id) -> <a href="./src/entity_python_sdk/types/entity_list_ancestor_organs_response.py">EntityListAncestorOrgansResponse</a></code>
- <code title="get /entities/{id}/collections">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_collections</a>(id, \*\*<a href="src/entity_python_sdk/types/entity_list_collections_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_list_collections_response.py">EntityListCollectionsResponse</a></code>
- <code title="get /entity-types">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_entity_types</a>() -> <a href="./src/entity_python_sdk/types/entity_list_entity_types_response.py">EntityListEntityTypesResponse</a></code>
- <code title="get /entities/{id}/siblings">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_siblings</a>(id, \*\*<a href="src/entity_python_sdk/types/entity_list_siblings_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_list_siblings_response.py">EntityListSiblingsResponse</a></code>
- <code title="get /entities/{id}/tuplets">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_tuplets</a>(id, \*\*<a href="src/entity_python_sdk/types/entity_list_tuplets_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_list_tuplets_response.py">EntityListTupletsResponse</a></code>
- <code title="get /entities/{id}/uploads">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">list_uploads</a>(id, \*\*<a href="src/entity_python_sdk/types/entity_list_uploads_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/entity_list_uploads_response.py">EntityListUploadsResponse</a></code>
- <code title="get /entities/{id}/provenance">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">retrieve_provenance</a>(id) -> None</code>
- <code title="get /entities/{id}">client.entities.<a href="./src/entity_python_sdk/resources/entities/entities.py">retrieve2</a>(id) -> <a href="./src/entity_python_sdk/types/entity.py">Entity</a></code>

## Type

Methods:

- <code title="get /entities/type/{type_a}/instanceof/{type_b}">client.entities.type.<a href="./src/entity_python_sdk/resources/entities/type.py">is_instance_of</a>(type_b, \*, type_a) -> <a href="./src/entity_python_sdk/types/instanceof.py">Instanceof</a></code>

# Ancestors

Types:

```python
from entity_python_sdk.types import AncestorRetrieveResponse
```

Methods:

- <code title="get /ancestors/{id}">client.ancestors.<a href="./src/entity_python_sdk/resources/ancestors.py">retrieve</a>(id) -> <a href="./src/entity_python_sdk/types/ancestor_retrieve_response.py">AncestorRetrieveResponse</a></code>

# Descendants

Types:

```python
from entity_python_sdk.types import DescendantRetrieveResponse
```

Methods:

- <code title="get /descendants/{id}">client.descendants.<a href="./src/entity_python_sdk/resources/descendants.py">retrieve</a>(id) -> <a href="./src/entity_python_sdk/types/descendant_retrieve_response.py">DescendantRetrieveResponse</a></code>

# Children

Types:

```python
from entity_python_sdk.types import ChildRetrieveResponse
```

Methods:

- <code title="get /children/{id}">client.children.<a href="./src/entity_python_sdk/resources/children.py">retrieve</a>(id) -> <a href="./src/entity_python_sdk/types/child_retrieve_response.py">ChildRetrieveResponse</a></code>

# Parents

Types:

```python
from entity_python_sdk.types import ParentRetrieveResponse
```

Methods:

- <code title="get /parents/{id}">client.parents.<a href="./src/entity_python_sdk/resources/parents.py">retrieve</a>(id) -> <a href="./src/entity_python_sdk/types/parent_retrieve_response.py">ParentRetrieveResponse</a></code>

# Doi

Methods:

- <code title="get /doi/redirect/{id}">client.doi.<a href="./src/entity_python_sdk/resources/doi.py">redirect</a>(id) -> None</code>

# Datasets

Types:

```python
from entity_python_sdk.types import (
    Dataset,
    File,
    Person,
    DatasetBulkUpdateResponse,
    DatasetCreateComponentsResponse,
    DatasetListDonorsResponse,
    DatasetListOrgansResponse,
    DatasetListSamplesResponse,
    DatasetListUnpublishedResponse,
    DatasetRetrieveMultiRevisionsResponse,
    DatasetRetrievePairedDatasetResponse,
    DatasetRetrieveProvMetadataResponse,
    DatasetRetrieveRevisionsResponse,
    DatasetRetrieveSankeyDataResponse,
)
```

Methods:

- <code title="put /datasets">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">bulk_update</a>(\*\*<a href="src/entity_python_sdk/types/dataset_bulk_update_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_bulk_update_response.py">DatasetBulkUpdateResponse</a></code>
- <code title="post /datasets/components">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">create_components</a>(\*\*<a href="src/entity_python_sdk/types/dataset_create_components_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_create_components_response.py">DatasetCreateComponentsResponse</a></code>
- <code title="get /datasets/{id}/donors">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">list_donors</a>(id) -> <a href="./src/entity_python_sdk/types/dataset_list_donors_response.py">DatasetListDonorsResponse</a></code>
- <code title="get /datasets/{id}/organs">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">list_organs</a>(id) -> <a href="./src/entity_python_sdk/types/dataset_list_organs_response.py">DatasetListOrgansResponse</a></code>
- <code title="get /datasets/{id}/samples">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">list_samples</a>(id) -> <a href="./src/entity_python_sdk/types/dataset_list_samples_response.py">DatasetListSamplesResponse</a></code>
- <code title="get /datasets/unpublished">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">list_unpublished</a>(\*\*<a href="src/entity_python_sdk/types/dataset_list_unpublished_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_list_unpublished_response.py">DatasetListUnpublishedResponse</a></code>
- <code title="put /datasets/{id}/retract">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retract</a>(id, \*\*<a href="src/entity_python_sdk/types/dataset_retract_params.py">params</a>) -> None</code>
- <code title="get /datasets/{id}/latest-revision">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_latest_revision</a>(id) -> <a href="./src/entity_python_sdk/types/dataset.py">Dataset</a></code>
- <code title="get /datasets/{id}/multi-revisions">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_multi_revisions</a>(id, \*\*<a href="src/entity_python_sdk/types/dataset_retrieve_multi_revisions_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_retrieve_multi_revisions_response.py">DatasetRetrieveMultiRevisionsResponse</a></code>
- <code title="get /datasets/{id}/paired-dataset">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_paired_dataset</a>(id, \*\*<a href="src/entity_python_sdk/types/dataset_retrieve_paired_dataset_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_retrieve_paired_dataset_response.py">DatasetRetrievePairedDatasetResponse</a></code>
- <code title="get /datasets/{id}/prov-metadata">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_prov_metadata</a>(id) -> <a href="./src/entity_python_sdk/types/dataset_retrieve_prov_metadata_response.py">DatasetRetrieveProvMetadataResponse</a></code>
- <code title="get /datasets/{id}/revision">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_revision</a>(id) -> None</code>
- <code title="get /datasets/{id}/revisions">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_revisions</a>(id, \*\*<a href="src/entity_python_sdk/types/dataset_retrieve_revisions_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/dataset_retrieve_revisions_response.py">DatasetRetrieveRevisionsResponse</a></code>
- <code title="get /datasets/sankey_data">client.datasets.<a href="./src/entity_python_sdk/resources/datasets/datasets.py">retrieve_sankey_data</a>() -> <a href="./src/entity_python_sdk/types/dataset_retrieve_sankey_data_response.py">DatasetRetrieveSankeyDataResponse</a></code>

## ProvInfo

Types:

```python
from entity_python_sdk.types.datasets import ProvInfoRetrieveResponse, ProvInfoListAllResponse
```

Methods:

- <code title="get /datasets/{id}/prov-info">client.datasets.prov_info.<a href="./src/entity_python_sdk/resources/datasets/prov_info.py">retrieve</a>(id, \*\*<a href="src/entity_python_sdk/types/datasets/prov_info_retrieve_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/datasets/prov_info_retrieve_response.py">ProvInfoRetrieveResponse</a></code>
- <code title="get /datasets/prov-info">client.datasets.prov_info.<a href="./src/entity_python_sdk/resources/datasets/prov_info.py">list_all</a>(\*\*<a href="src/entity_python_sdk/types/datasets/prov_info_list_all_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/datasets/prov_info_list_all_response.py">ProvInfoListAllResponse</a></code>

# Uploads

Types:

```python
from entity_python_sdk.types import UploadUpdateBulkResponse
```

Methods:

- <code title="put /uploads">client.uploads.<a href="./src/entity_python_sdk/resources/uploads.py">update_bulk</a>(\*\*<a href="src/entity_python_sdk/types/upload_update_bulk_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/upload_update_bulk_response.py">UploadUpdateBulkResponse</a></code>

# Samples

Types:

```python
from entity_python_sdk.types import SampleRetrieveProvInfoResponse
```

Methods:

- <code title="get /samples/prov-info">client.samples.<a href="./src/entity_python_sdk/resources/samples.py">retrieve_prov_info</a>(\*\*<a href="src/entity_python_sdk/types/sample_retrieve_prov_info_params.py">params</a>) -> <a href="./src/entity_python_sdk/types/sample_retrieve_prov_info_response.py">SampleRetrieveProvInfoResponse</a></code>

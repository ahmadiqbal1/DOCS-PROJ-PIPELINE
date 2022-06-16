# Pipeline Instance

```python
pipeline_instance_controller = client.pipeline_instance
```

## Class Name

`PipelineInstanceController`

## Methods

* [Pipeline Controller Add New Pipeline](../../doc/controllers/pipeline-instance.md#pipeline-controller-add-new-pipeline)
* [Pipeline Controller Delete Pieline](../../doc/controllers/pipeline-instance.md#pipeline-controller-delete-pieline)


# Pipeline Controller Add New Pipeline

```python
def pipeline_controller_add_new_pipeline(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PipelineDto`](../../doc/models/pipeline-dto.md) | Body, Required | - |

## Response Type

[`PipelineDto`](../../doc/models/pipeline-dto.md)

## Example Usage

```python
body = PipelineDto()
body.id = 'id6'
body.pipeline_id = 'pipelineId0'
body.project_id = 'projectId6'
body.owner_id = 'ownerId2'

result = pipeline_instance_controller.pipeline_controller_add_new_pipeline(body)
```


# Pipeline Controller Delete Pieline

```python
def pipeline_controller_delete_pieline(self,
                                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
id = 'id0'

result = pipeline_instance_controller.pipeline_controller_delete_pieline(id)
```


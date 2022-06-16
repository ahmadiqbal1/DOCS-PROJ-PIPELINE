# Project

```python
project_controller = client.project
```

## Class Name

`ProjectController`

## Methods

* [Project Controller Add New Project Member](../../doc/controllers/project.md#project-controller-add-new-project-member)
* [Project Controller Add New Project](../../doc/controllers/project.md#project-controller-add-new-project)
* [Project Controller Edit Project](../../doc/controllers/project.md#project-controller-edit-project)
* [Project Controller Get Project by Owner Id](../../doc/controllers/project.md#project-controller-get-project-by-owner-id)
* [Project Controller Get Pipelines Count by Project Id](../../doc/controllers/project.md#project-controller-get-pipelines-count-by-project-id)
* [Project Controller Find All Pipelines by Project Id](../../doc/controllers/project.md#project-controller-find-all-pipelines-by-project-id)
* [Project Controller Get Project Statistics](../../doc/controllers/project.md#project-controller-get-project-statistics)
* [Project Controller Get All Project Statistics](../../doc/controllers/project.md#project-controller-get-all-project-statistics)
* [Project Controller Get Project by User Idand Project Id](../../doc/controllers/project.md#project-controller-get-project-by-user-idand-project-id)
* [Project Controller Delete Project Member](../../doc/controllers/project.md#project-controller-delete-project-member)
* [Project Controller Delete Project](../../doc/controllers/project.md#project-controller-delete-project)


# Project Controller Add New Project Member

```python
def project_controller_add_new_project_member(self,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateProjectMemberDto`](../../doc/models/create-project-member-dto.md) | Body, Required | - |

## Response Type

[`ProjectMemberDto`](../../doc/models/project-member-dto.md)

## Example Usage

```python
body = CreateProjectMemberDto()

result = project_controller.project_controller_add_new_project_member(body)
```


# Project Controller Add New Project

```python
def project_controller_add_new_project(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateProjectDto`](../../doc/models/create-project-dto.md) | Body, Required | - |

## Response Type

[`ProjectDto`](../../doc/models/project-dto.md)

## Example Usage

```python
body = CreateProjectDto()

result = project_controller.project_controller_add_new_project(body)
```


# Project Controller Edit Project

```python
def project_controller_edit_project(self,
                                   project_id,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `string` | Template, Required | - |
| `body` | [`UpdateProjectDto`](../../doc/models/update-project-dto.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
project_id = 'projectId0'
body = UpdateProjectDto()

result = project_controller.project_controller_edit_project(project_id, body)
```


# Project Controller Get Project by Owner Id

```python
def project_controller_get_project_by_owner_id(self,
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

result = project_controller.project_controller_get_project_by_owner_id(id)
```


# Project Controller Get Pipelines Count by Project Id

```python
def project_controller_get_pipelines_count_by_project_id(self,
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

result = project_controller.project_controller_get_pipelines_count_by_project_id(id)
```


# Project Controller Find All Pipelines by Project Id

```python
def project_controller_find_all_pipelines_by_project_id(self,
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

result = project_controller.project_controller_find_all_pipelines_by_project_id(id)
```


# Project Controller Get Project Statistics

```python
def project_controller_get_project_statistics(self,
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

result = project_controller.project_controller_get_project_statistics(id)
```


# Project Controller Get All Project Statistics

```python
def project_controller_get_all_project_statistics(self,
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

result = project_controller.project_controller_get_all_project_statistics(id)
```


# Project Controller Get Project by User Idand Project Id

```python
def project_controller_get_project_by_user_idand_project_id(self,
                                                           user_id,
                                                           project_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |
| `project_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'
project_id = 'projectId0'

result = project_controller.project_controller_get_project_by_user_idand_project_id(user_id, project_id)
```


# Project Controller Delete Project Member

```python
def project_controller_delete_project_member(self,
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

result = project_controller.project_controller_delete_project_member(id)
```


# Project Controller Delete Project

```python
def project_controller_delete_project(self,
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

result = project_controller.project_controller_delete_project(id)
```


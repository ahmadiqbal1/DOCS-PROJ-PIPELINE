# Templatesand User Authorization

```python
templatesand_user_authorization_controller = client.templatesand_user_authorization
```

## Class Name

`TemplatesandUserAuthorizationController`

## Methods

* [Template Accessibility Controller Add New Template](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-add-new-template)
* [Template Accessibility Controller Edit Template Permissions](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-edit-template-permissions)
* [Template Accessibility Controller Delete Template](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-delete-template)
* [Template Accessibility Controller Give Access Permission by Template Id](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-give-access-permission-by-template-id)
* [Template Accessibility Controller Get All Auth Users](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-all-auth-users)
* [Template Accessibility Controller Get Allpublic Pipelines](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-allpublic-pipelines)
* [Template Accessibility Controller Get Templates by User Id](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-templates-by-user-id)
* [Template Accessibility Controller Get Pipelines Details](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-pipelines-details)
* [Template Accessibility Controller Get Plugins Details](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-plugins-details)
* [Template Accessibility Controller Get Template Details](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-template-details)
* [Template Accessibility Controller Get Template Statistcs](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-get-template-statistcs)
* [Template Accessibility Controller Delete User](../../doc/controllers/templatesand-user-authorization.md#template-accessibility-controller-delete-user)


# Template Accessibility Controller Add New Template

```python
def template_accessibility_controller_add_new_template(self,
                                                      template_type,
                                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_type` | `string` | Query, Required | - |
| `body` | [`CreateTemplateDto`](../../doc/models/create-template-dto.md) | Body, Required | - |

## Response Type

[`TemplateDto`](../../doc/models/template-dto.md)

## Example Usage

```python
template_type = 'Template_Type4'
body = CreateTemplateDto()

result = templates_and_user_authorization_controller.template_accessibility_controller_add_new_template(template_type, body)
```


# Template Accessibility Controller Edit Template Permissions

```python
def template_accessibility_controller_edit_template_permissions(self,
                                                               template_id,
                                                               access_modifier)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_id` | `string` | Template, Required | - |
| `access_modifier` | `string` | Query, Required | - |

## Response Type

`void`

## Example Usage

```python
template_id = 'templateId0'
access_modifier = 'AccessModifier8'

result = templates_and_user_authorization_controller.template_accessibility_controller_edit_template_permissions(template_id, access_modifier)
```


# Template Accessibility Controller Delete Template

```python
def template_accessibility_controller_delete_template(self,
                                                     template_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
template_id = 'templateId0'

result = templates_and_user_authorization_controller.template_accessibility_controller_delete_template(template_id)
```


# Template Accessibility Controller Give Access Permission by Template Id

```python
def template_accessibility_controller_give_access_permission_by_template_id(self,
                                                                           template_id,
                                                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_id` | `string` | Template, Required | - |
| `body` | `List of string` | Body, Required | - |

## Response Type

[`AuthorizedUserDto`](../../doc/models/authorized-user-dto.md)

## Example Usage

```python
template_id = 'templateId0'
body = ['body4', 'body5']

result = templates_and_user_authorization_controller.template_accessibility_controller_give_access_permission_by_template_id(template_id, body)
```


# Template Accessibility Controller Get All Auth Users

```python
def template_accessibility_controller_get_all_auth_users(self,
                                                        template_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
template_id = 'templateId0'

result = templates_and_user_authorization_controller.template_accessibility_controller_get_all_auth_users(template_id)
```


# Template Accessibility Controller Get Allpublic Pipelines

```python
def template_accessibility_controller_get_allpublic_pipelines(self)
```

## Response Type

`void`

## Example Usage

```python
result = templates_and_user_authorization_controller.template_accessibility_controller_get_allpublic_pipelines()
```


# Template Accessibility Controller Get Templates by User Id

```python
def template_accessibility_controller_get_templates_by_user_id(self,
                                                              user_id,
                                                              template_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |
| `template_type` | `string` | Query, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'
template_type = 'Template_Type4'

result = templates_and_user_authorization_controller.template_accessibility_controller_get_templates_by_user_id(user_id, template_type)
```


# Template Accessibility Controller Get Pipelines Details

```python
def template_accessibility_controller_get_pipelines_details(self,
                                                           ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List of string` | Query, Optional | - |

## Response Type

`void`

## Example Usage

```python
result = templates_and_user_authorization_controller.template_accessibility_controller_get_pipelines_details()
```


# Template Accessibility Controller Get Plugins Details

```python
def template_accessibility_controller_get_plugins_details(self,
                                                         with_config,
                                                         ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `with_config` | `bool` | Query, Required | - |
| `ids` | `List of string` | Query, Optional | - |

## Response Type

`void`

## Example Usage

```python
with_config = False

result = templates_and_user_authorization_controller.template_accessibility_controller_get_plugins_details(with_config)
```


# Template Accessibility Controller Get Template Details

```python
def template_accessibility_controller_get_template_details(self,
                                                          user_id,
                                                          template_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |
| `template_type` | `string` | Query, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'
template_type = 'Template_Type4'

result = templates_and_user_authorization_controller.template_accessibility_controller_get_template_details(user_id, template_type)
```


# Template Accessibility Controller Get Template Statistcs

```python
def template_accessibility_controller_get_template_statistcs(self,
                                                            user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'

result = templates_and_user_authorization_controller.template_accessibility_controller_get_template_statistcs(user_id)
```


# Template Accessibility Controller Delete User

```python
def template_accessibility_controller_delete_user(self,
                                                 template_id,
                                                 user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_id` | `string` | Template, Required | - |
| `user_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
template_id = 'templateId0'
user_id = 'userId0'

result = templates_and_user_authorization_controller.template_accessibility_controller_delete_user(template_id, user_id)
```


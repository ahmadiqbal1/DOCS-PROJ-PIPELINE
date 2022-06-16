# Documentation

```python
documentation_controller = client.documentation
```

## Class Name

`DocumentationController`

## Methods

* [Documentation Controller Add New Article](../../doc/controllers/documentation.md#documentation-controller-add-new-article)
* [Documentation Controller Get All Articles](../../doc/controllers/documentation.md#documentation-controller-get-all-articles)
* [Documentation Controller Edit Article](../../doc/controllers/documentation.md#documentation-controller-edit-article)
* [Documentation Controller Get Article by Id](../../doc/controllers/documentation.md#documentation-controller-get-article-by-id)
* [Documentation Controller Delete Article by Id](../../doc/controllers/documentation.md#documentation-controller-delete-article-by-id)
* [Documentation Controller Get Articles by Author Id](../../doc/controllers/documentation.md#documentation-controller-get-articles-by-author-id)
* [Documentation Controller Get Articles by Type](../../doc/controllers/documentation.md#documentation-controller-get-articles-by-type)
* [Documentation Controller Get Articles by Catogory](../../doc/controllers/documentation.md#documentation-controller-get-articles-by-catogory)


# Documentation Controller Add New Article

```python
def documentation_controller_add_new_article(self,
                                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateArticleDto`](../../doc/models/create-article-dto.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = CreateArticleDto()

result = documentation_controller.documentation_controller_add_new_article(body)
```


# Documentation Controller Get All Articles

```python
def documentation_controller_get_all_articles(self)
```

## Response Type

`void`

## Example Usage

```python
result = documentation_controller.documentation_controller_get_all_articles()
```


# Documentation Controller Edit Article

```python
def documentation_controller_edit_article(self,
                                         id,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | - |
| `body` | [`CreateArticleDto`](../../doc/models/create-article-dto.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
id = 'id0'
body = CreateArticleDto()

result = documentation_controller.documentation_controller_edit_article(id, body)
```


# Documentation Controller Get Article by Id

```python
def documentation_controller_get_article_by_id(self,
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

result = documentation_controller.documentation_controller_get_article_by_id(id)
```


# Documentation Controller Delete Article by Id

```python
def documentation_controller_delete_article_by_id(self,
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

result = documentation_controller.documentation_controller_delete_article_by_id(id)
```


# Documentation Controller Get Articles by Author Id

```python
def documentation_controller_get_articles_by_author_id(self,
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

result = documentation_controller.documentation_controller_get_articles_by_author_id(id)
```


# Documentation Controller Get Articles by Type

```python
def documentation_controller_get_articles_by_type(self,
                                                 mtype)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
mtype = 'type0'

result = documentation_controller.documentation_controller_get_articles_by_type(mtype)
```


# Documentation Controller Get Articles by Catogory

```python
def documentation_controller_get_articles_by_catogory(self,
                                                     catogory)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catogory` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
catogory = 'catogory4'

result = documentation_controller.documentation_controller_get_articles_by_catogory(catogory)
```


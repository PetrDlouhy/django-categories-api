# Django Categories

[![codecov](https://codecov.io/gh/petrdlouhy/django-categories-api/branch/master/graph/badge.svg?token=rW8mpdZqWQ)](https://codecov.io/gh/petrdlouhy/django-categories-api)
[![Run Tox tests](https://github.com/PetrDlouhy/django-categories-api/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/PetrDlouhy/django-categories-api/actions/workflows/run-tests.yaml)
[![Run Tox tests](https://img.shields.io/pypi/v/django-categories-api.svg)](https://pypi.python.org/pypi/django-categories-api/)

This application provides basic ``django-rest-framework`` API for Django Categories.


## Features of the project

The output contains category tree with counts of category items in each node (cummulative as well as direct counts).


## Countable fields

The API can contain number of related objects associatet with category.
This can be achieved by setting ``COUNTABLE_FIELD_RELATED_NAMES`` property in ``CATEGORIES_SETTINGS``:

```python
  CATEGORIES_SETTINGS = {
      "COUNTABLE_FIELD_RELATED_NAMES": ('field_name'),
  }
```

## Settings

The cache timeout and staggering can be changed by:

```python
  CATEGORIES_SETTINGS = {
      "CACHE_TIMEOUT": 60 * 60,
      "CACHE_STAGGERING": 60 * 10,
  }
```

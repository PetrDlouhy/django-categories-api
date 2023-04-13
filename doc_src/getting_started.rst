===============
Getting Started
===============


Adding Django Rest framework API endpoint
=========================================


Registering the API
*******************

If you have installed Django REST framework, all you have to do is add categories router to your router:

.. code-block:: python

   from rest_framework.routers import DefaultRouter
   from categories.api.urls import router as category_router

   router = DefaultRouter()
   router.registry.extend(category_router.registry)


Overriding the API
******************

If you want to modify the API, you can register your own overriden viewset:

.. code-block:: python

    from categories.api.viewsets import CategoryViewSet


    class LimitedCategoryViewSet(CategoryViewSet):
        extra_count_filters = {"verification_status": "validated"}


    router.register(r"categories", LimitedCategoryViewSet, basename="categories")

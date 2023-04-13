from rest_framework.routers import DefaultRouter

from categories_api.urls import router as category_router

router = DefaultRouter()
router.registry.extend(category_router.registry)

urlpatterns = router.urls

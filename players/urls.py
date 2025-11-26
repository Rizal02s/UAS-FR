from rest_framework.routers import DefaultRouter
from .views import PemainViewSet

router = DefaultRouter()
router.register(r'players', PemainViewSet, basename='pemain')

urlpatterns = router.urls
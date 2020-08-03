from rest_framework import routers
from .api import BuyerViewSet

router = routers.DefaultRouter()
router.register('api/buyers', BuyerViewSet, 'buyers')

urlpatterns = router.urls

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductsView)
router.register(r'carthistory', CartHistoryView)
router.register(r'productbought', ProductBoughtView)

urlpatterns = router.urls

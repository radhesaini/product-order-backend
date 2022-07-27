from rest_framework.routers import SimpleRouter
from core import views


router = SimpleRouter()

router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'csvfile', views.CsvFileViewSet)

urlpatterns = router.urls

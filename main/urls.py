from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('imagewords', views.ImageWordViewSet)

urlpatterns = router.urls

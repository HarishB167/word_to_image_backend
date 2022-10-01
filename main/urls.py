from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('imagewords', views.ImageWordViewSet)

urlpatterns = router.urls

urlpatterns += [path('get_images_for_words/', views.get_images_for_words)]

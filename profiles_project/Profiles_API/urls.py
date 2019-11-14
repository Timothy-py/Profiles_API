from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UselProfileViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
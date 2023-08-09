from django.urls import include, path
from . import views
from rest_framework import routers
from .views import PostViewSet, StatusViewSet, TreesViewSet

router = routers.DefaultRouter()
router.register('postView', PostViewSet)
router.register('trees', TreesViewSet)
router.register('status', StatusViewSet)

urlpatterns = [
    path('create', views.post_create, name='create'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
    path('', include(router.urls)),
]
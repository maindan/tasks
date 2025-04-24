from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register("task", views.TaskViewSet, basename="Tasks")

urlpatterns = [
    path("", include(router.urls))
]
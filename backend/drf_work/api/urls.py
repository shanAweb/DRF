from django.urls import path

from . import views
urlpatterns = [
    path('health', views.get_status),
    path('data', views.endpoint_view),
]
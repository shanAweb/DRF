from django.urls import path

from . import views
urlpatterns = [
    path('data', views.endpoint_view),
    path('health', views.get_status),
]
from django.urls import path

from . import views
urlpatterns = [
    path('health', views.get_status),
    path('check', views.endpoint_view),
    path('data', views.manage_data),
]
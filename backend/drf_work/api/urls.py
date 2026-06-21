from django.urls import path

from . import views
urlpatterns = [
    path('', views.endpoint_view)
]
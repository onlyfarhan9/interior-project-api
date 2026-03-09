from django.urls import path
from . import views


urlpatterns = [
    path("furniture-details/",views.furniture_details)
]
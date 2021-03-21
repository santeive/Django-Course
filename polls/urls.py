from django.urls import path
from . import views

# We create the urls.py file
urlpatterns = [
    path('', views.index, name="index")
]
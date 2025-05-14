from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('api/lecturers', fetch_lecturers)
]

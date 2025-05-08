from django.urls import path
from .views import login_view, logout_view, get_csrf, current_user

from . import views

urlpatterns = [
    path('api/csrf/', get_csrf),
    path('api/login/', login_view),
    path('api/logout/', logout_view),
    path('api/user/', current_user),
]

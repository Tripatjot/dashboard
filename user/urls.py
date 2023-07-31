from django.urls import path, include
from .views import *

urlpatterns = [
    path('createuser', create_user.as_view()),
    path('getusers/<int:pk>', get_users.as_view()),
    path('updateuser/<int:pk>', update_user.as_view()),
    path('deleteuser/<int:pk>', delete_user.as_view()),
]
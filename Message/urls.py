from django.urls import path
from .views import *

urlpatterns=[
    path('message/<int:id>',chatroom)
]
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',show_post ),
    path('new_post/',new_post),
    path('save_comment/<int:id>/',save_comment),
    path('like/<int:id>',like)
]
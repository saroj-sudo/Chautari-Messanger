
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', include('Post.urls')),
    path('admin/',admin.site.urls),
    path('register/',register),
    path('login/',login_me),
    path('friend/',include('Friend.urls')),
    path('message/',include('Message.urls')),
    
    
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', views.chat, name="chat"),
    path('chat/<str:room_name>/', views.room, name="room"),
]

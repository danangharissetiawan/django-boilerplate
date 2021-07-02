from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<filename>', views.home_files, name='home-files'),
]

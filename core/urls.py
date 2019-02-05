from django.urls import path

from core import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page')
]

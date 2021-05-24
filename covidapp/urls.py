from django.urls import path

from . import views
urlpatterns = [
    path('', views.hellowordview, name='helloword'),
]
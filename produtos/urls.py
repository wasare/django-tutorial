from django.urls import path

from produtos.views import index, ola

urlpatterns = [
    path('index/', index ,name="index"),
    path('ola/', ola , name="ola"),
]
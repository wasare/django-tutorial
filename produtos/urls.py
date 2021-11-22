from django.urls import path

from produtos.views import (
    index, ola,
    CreateCategoryView,
    ListCategoryView,
)

urlpatterns = [
    path('', index ,name="index"),
    path('ola/', ola , name="ola"),
    path('category/add',
            CreateCategoryView.as_view(),
            name='create_category',
        ),
    path('category',
            ListCategoryView.as_view(),
            name='list_category',
        )
]
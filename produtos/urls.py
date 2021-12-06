from django.urls import path

from produtos.views import (
    index, ola,
    CreateCategoryView,
    ListCategoryView,
    DetailCategoryView,
    UpdateCategoryView,
    DeleteCategoryView,
)

urlpatterns = [
    path('', index ,name="index"),
    path('ola/', ola , name="ola"),
    path('category/add',
            CreateCategoryView.as_view(),
            name='category_create',
        ),
    path('category',
            ListCategoryView.as_view(),
            name='category_list',
        ),
    path('category/<int:pk>',
            DetailCategoryView.as_view(),
            name='category_detail'),
    path('category/<int:pk>/update',
            UpdateCategoryView.as_view(),
            name="category_update"),
    path('category/<int:pk>/delete',
            DeleteCategoryView.as_view(),
            name="category_delete"),
]
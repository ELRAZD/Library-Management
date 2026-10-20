from django.urls import path
from library.views import *

urlpatterns = [
    path('author_create/', author_create, name='author_create'),
    path('author_list/', author_list, name='author_list'),
    path('author_details/<str:a_id>/', author_details, name='author_details'),
    path('author_update/<str:a_id>/', author_update, name='author_update'),
    path('author_delete/<str:a_id>/', author_delete, name='author_delete'),


    path('book_create/', book_create, name='book_create'),
    path('book_list/', book_list, name='book_list'),
    path('book_details/<str:b_id>/', book_details, name='book_details'),
    path('book_update/<str:b_id>/', book_update, name='book_update'),
    path('book_delete/<str:b_id>/', book_delete, name='book_delete'),


    path('borrow_create/', borrow_create, name='borrow_create'),
    path('borrow_list/', borrow_list, name='borrow_list'),
    path('borrow_details/<str:br_id>/', borrow_details, name='borrow_details'),
    path('borrow_update/<str:br_id>/', borrow_update, name='borrow_update'),
    path('borrow_delete/<str:br_id>/', borrow_delete, name='borrow_delete'),


    path('category_create/', category_create, name='category_create'),
    path('category_list/', category_list, name='category_list'),
    path('category_details/<str:c_id>/', category_details, name='category_details'),
    path('category_update/<str:c_id>/', category_update, name='category_update'),
    path('category_delete/<str:c_id>/', category_delete, name='category_delete'),
]
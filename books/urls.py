from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('category/create', views.CategoryCreateView.as_view(), name='category-create'),
    path('success/', views.success, name='success'),
    # path('', views.BookList.as_view(), name='book.all'),
    # path('', include('django.contrib.auth.urls')),

]

from django.urls import path
from . import views

urlpatterns =[
    path('posts/', views.PostList.as_view(), name='postlist'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('post/create/', views.PostCreate.as_view(), name='postcreate'),
]
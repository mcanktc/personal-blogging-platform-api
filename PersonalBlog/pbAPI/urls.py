from django.urls import path
from . import views

urlpatterns =[
    path('posts/', views.PostList.as_view(), name='postlist'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('posts/create/', views.PostCreate.as_view(), name='postcreate'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='postdelete'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='postupdate')
]
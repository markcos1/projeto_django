from django.urls import path
from .views import PostList, PostDetail, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]


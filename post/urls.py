from django.urls import path
from .views import PostList, PostDetail



app_name = "post"

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:id>/', PostDetail.as_view(), name='post'),
]

from django.urls import path
from .views import PostList, PostDetail



app_name = "pay"

urlpatterns = [
    path('', PostList.as_view(), name='pays'),
    path('<int:id>/', PostDetail.as_view(), name='pay'),
]

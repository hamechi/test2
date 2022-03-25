from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Most, Post
from .permissions import IsAuthenticatedVerified
from .serializers import MostSerializer, PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects
    serializer_class = PostSerializer
    lookup_field = "id"

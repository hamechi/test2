from .models import Bost, Cost
from .serializers import PostSerializer, MostSerializer
from rest_framework import generics


from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostList(generics.ListCreateAPIView):
    queryset = Bost.objects.all()
    serializer_class = PostSerializer





class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bost.objects
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = "id"

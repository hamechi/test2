from rest_framework import serializers
from .models import Post, Most


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        exclude = ['is_deleted']


class MostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Most
        #fields = '__all__'
        exclude = ['is_deleted']

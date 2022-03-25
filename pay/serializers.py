from rest_framework import serializers

from .models import Bost, Cost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bost
        #fields = '__all__'
        exclude = ['is_deleted']


class MostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        #fields = '__all__'
        exclude = ['is_deleted']

from rest_framework.serializers import ModelSerializer
from todos.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'desc', 'is_complete',)
        #exclude = ['id', 'owner', 'created_at', 'updated_at']

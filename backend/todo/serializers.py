from rest_framework import serializers
from .models import Todo
# need serializers to convert model instances to JSON so that the frontend can work with the received data.

# This code specifies the model to work with and the fields to be converted to JSON.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
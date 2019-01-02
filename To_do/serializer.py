from rest_framework import serializers

from To_do.models import ToDo

#serializer = turning model data -> JSON
class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ('id', 'text', 'done')
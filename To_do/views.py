from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters



from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from To_do.models import ToDo
from To_do.serializer import ToDoSerializer

class ToDoListView(APIView):
	def get(self, request):
 
		#request is not standard http request, it's the rest one
		#you can see the data it has by doing request.data
		#should return a {}
		todos = ToDo.objects.all()
		#Actually need to pass through a query set
		#many, tells if it is just a single object or a list
		serializer = ToDoSerializer(todos, many=True)
		#filter_backends = (filters.SearchFilter,)
		#search_fields = ('text', 'done')
		
		return Response(serializer.data)

	

	def put(self, request):

		serializer = ToDoSerializer(data=request.data)
		#checks if the data is valid and the request words
		if serializer.is_valid():
			serializer.save()
			#saves to database!!
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		#if it is not valid raise an error, a bad request errer
		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

class ToDoDetailedView(APIView):
	def get(self, request, pk):
		#gets object or raise 404 error
		todo = get_object_or_404(ToDo, pk=pk)
		serializer = ToDoSerializer(todo)
		return Response(serializer.data)

	def delete(self, request, pk):
		#because it's detailed view it has direct access to object
		todo = get_object_or_404(ToDo, pk=pk)
		#deletes an object from database
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

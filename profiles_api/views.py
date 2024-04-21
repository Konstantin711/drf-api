from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, path)',
            'Is similar to a traditional Django View',
            'Gives you xthe most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Response', 'an_apiview': an_apiview})
    

    def post(self, request):
        "Creates a hello message with name field"

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response(dict(message=message))
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
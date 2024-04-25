from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status
from profiles_api import serializers, models


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
    


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer 

    def list(self, request):
        """Return hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response(
            dict(
                message='Hello',
                a_viewset=a_viewset
            )
        )
    
    def create(self, request):
        """Create new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def retrieve(self, request, pk=None):
        """Handle getting an obj by its ID(pk)"""

        return Response(
            dict(
                view_method='retrieve() - get specified obj',
                http_method=request.method
            )
        )
    
    def update(self, request, pk=None):
        """Handle update of obj by its ID(pk)"""

        return Response(
            dict(
                view_method='update() - get specified obj',
                http_method=request.method
            )
        )
    

    def partial_update(self, request, pk=None):
        """Handle update of obj by its ID(pk)"""

        return Response(
            dict(
                view_method='partial_update() - update obj partially',
                http_method=request.method
            )
        )
    

    def delete(self, request, pk=None):
        """Handle update of obj by its ID(pk)"""

        return Response(
            dict(
                view_method='delete() - update obj partially',
                http_method=request.method
            )
        )
    

class UselProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
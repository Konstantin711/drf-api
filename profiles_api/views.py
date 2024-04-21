from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, path)',
            'Is similar to a traditional Django View',
            'Gives you xthe most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Response', 'an_apiview': an_apiview})

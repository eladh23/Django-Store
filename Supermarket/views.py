from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    api_endpoints = {
        "message": "Welcome to my Django API!",
    }
    return Response(api_endpoints) 
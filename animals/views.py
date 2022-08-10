from urllib.request import Request
from django.shortcuts import get_list_or_404

from rest_framework.views import APIView, Request, Response
from rest_framework import status

from animals.models import Animal
from .serializers import AnimalSerializer

class AnimalView(APIView):
    def get(self, request: Request) -> Response:
        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)


    def post(self, request: Request) -> Response:
        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)





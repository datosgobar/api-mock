from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def landing(request):
    return render(request, 'landing.html')


@api_view(['POST'])
def echo(request):
    return Response(request.data)

import re

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def landing(request):
    return render(request, 'landing.html')


@api_view(['POST'])
def echo(request):
    return Response(request.data)


@api_view(['GET'])
def datos_csv(_):
    return Response(b'id, username\n 1, lauren\n 2, john')


DATA = [{'id': 1, 'username': 'lauren'},
        {'id': 2, 'username': 'john'}]


@api_view(['GET'])
def datos_json(request):
    response_data = DATA.copy()

    if 'q' in request.query_params:
        pattern = request.query_params['q']
        response_data = filter(lambda x: re.match(pattern, x['username']), response_data)

    if 'only_id' in request.query_params \
            and request.query_params['only_id'].lower() == 'true':
        response_data = map(lambda x: x['id'], response_data)

    response_data = list(response_data)
    return Response({'total': len(response_data),
                     'data': response_data})

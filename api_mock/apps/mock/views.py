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

  
@api_view(['GET']) 
def datos_json(request):
    if 'only_id' in request.query_params \
            and request.query_params['only_id'].lower() == 'true':
        response_data = {'total': 2,
                         'data': [1, 2]}
    else:
        response_data = {'total': 2,
                         'data': [{'id': 1,
                                   'username': 'lauren'},
                                  {'id': 2,
                                   'username': 'john'}]}

    return Response(response_data)

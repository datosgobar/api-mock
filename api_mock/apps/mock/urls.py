from django.urls import path

import api_mock.apps.mock.views as views

# pylint: disable=invalid-name
urlpatterns = [
    path('echo/', views.echo, name='echo'),
    path('', views.landing),
]

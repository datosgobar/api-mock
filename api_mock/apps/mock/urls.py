from django.urls import path

import api_mock.apps.mock.views as views

# pylint: disable=invalid-name
urlpatterns = [
    path('echo/', views.echo, name='echo'),
    path('datos.csv/', views.datos_csv, name='datos.csv'),
    path('datos.json/', views.datos_json, name='datos.json'),
    path('docs/oai_specification.yml', views.oai_specification_yml, name='oai_yml'),
    path('docs/oai_specification.json', views.oai_specification_json, name='oai_json'),
    path('', views.landing),
]

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiMockTests(APITestCase):

    def test_echo(self):

        url = reverse('echo')
        data = {'arg': 'val'}

        response = self.client.post(url, data, format='json')
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json, data)

    def test_get_datos_json(self):

        url = reverse('datos.json')

        response = self.client.get(url)

        self.assertEqual(response.json(), {'total': 2,
                                           'data': [{'id': 1,
                                                     'username': 'lauren'},
                                                    {'id': 2,
                                                     'username': 'john'}]})

    def test_get_datos_json_only_id(self):

        url = reverse('datos.json')

        query = {'only_id': True}

        response = self.client.get(url, data=query)

        self.assertEqual(response.json(), {'total': 2,
                                           'data': [1, 2]})

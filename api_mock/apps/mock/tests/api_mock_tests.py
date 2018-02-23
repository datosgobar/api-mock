from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiMockTests(APITestCase):

    def setUp(self):
        self.expected_datos_json = {'total': 2,
                                    'data': [{'id': 1,
                                              'username': 'lauren'},
                                             {'id': 2,
                                              'username': 'john'}]}
        self.expected_datos_json_only_id = {'total': 2,
                                            'data': [1, 2]}

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

        self.assertEqual(response.json(), self.expected_datos_json)

    def test_get_datos_csv(self):

        url = reverse('datos.csv')

        response = self.client.get(url)

        expected_data = b'"id, username\\n 1, lauren\\n 2, john"'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, expected_data)

    def test_get_datos_json_only_id(self):

        url = reverse('datos.json')

        query = {'only_id': True}

        response = self.client.get(url, data=query)

        self.assertEqual(response.json(), self.expected_datos_json_only_id)

    def test_get_datos_json_only_id_false(self):  # pylint: disable=invalid-name

        url = reverse('datos.json')

        query = {'only_id': False}

        response = self.client.get(url, data=query)

        self.assertEqual(response.json(), self.expected_datos_json)

    def test_get_datos_json_q(self):

        url = reverse('datos.json')

        query = {'q': 'lauren'}

        response = self.client.get(url, data=query)

        self.assertEqual(response.json(), {'total': 1,
                                           'data': [{'id': 1,
                                                     'username': 'lauren'}]})

    def test_get_datos_json_q_only_id_true(self):

        url = reverse('datos.json')

        query = {'q': 'lauren',
                 'only_id': True}

        response = self.client.get(url, data=query)

        self.assertEqual(response.json(), {'total': 1,
                                           'data': [1]})
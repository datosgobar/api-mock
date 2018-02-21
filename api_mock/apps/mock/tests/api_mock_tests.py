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

    def test_get_data(self):

        url = reverse('data')

        response = self.client.get(url)

        self.assertEqual(response.json(), {'id': 4, 'username': 'lauren'})

    def test_get_datos_csv(self):

        url = reverse('datos.csv')

        response = self.client.get(url)

        expected_data = b'"id, username\\n 1, lauren\\n 2, john"'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, expected_data)

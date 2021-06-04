from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from rest_framework.test import APITestCase


def _has_user(username: str, **kwargs) -> Type[AbstractUser]:
    return get_user_model().objects.filter(username=username, **kwargs).exists()


class TestUserCreation(APITestCase):

    def setUp(self) -> None:
        self.client = self.client_class()
        self.test_user = get_user_model().objects.create_user(username='TempUser',
                                                              password='temp_password_123')

    def test_user_creation(self):
        """
        Test for user creation, should create user
        """
        user_creation_url = reverse('user_view')
        user_creation_payload = {'username': 'Temp',
                                 'password': 'temp_password_1123',
                                 'email': 'g@g.com'}

        response = self.client.post(path=user_creation_url, data=user_creation_payload)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(_has_user(username='Temp'))

    def test_user_creation_bad_password(self):
        user_creation_url = reverse('user_view')
        user_creation_payload = {'username': 'Temp',
                                 'password': 'password'}

        response = self.client.post(path=user_creation_url, data=user_creation_payload)

        self.assertEqual(response.status_code, 400)

    def test_get_user_data(self):
        user_data_url = reverse('user_view')
        self.client.force_authenticate(self.test_user)

        response = self.client.get(user_data_url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('username', response.data)
        self.assertEqual(response.data['username'], 'TempUser')

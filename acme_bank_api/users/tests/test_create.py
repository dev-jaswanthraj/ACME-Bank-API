from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class UsersTest(APITestCase):
    """ Test the User Model and It's Endpoints """

    def test_create_user(self):
        """ User Creation Test without Error """

        data = {
          'username': 'frescoplayuser',
          'email': 'frescouser@tcs.com',
          'password': 'test12345'
        }

        # Post Method
        response = self.client.post(
          reverse('user-create'),
          data,
          format='json'
        )

        # Query for get the latest user
        user = User.objects.all().order_by("-id")[0]

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

        # To verify token
        token = Token.objects.get(user=user)

        self.assertEqual(response.data['token'], token.key)

    def test_user_with_error(self):
        """ User Creation Test with Error """

        data = {
          'username': 'frescoplayuser',
          'email': 'frescouser@tcscom',
          'password': 'test124'
        }

        # Post 
        response = self.client.post(
          reverse('user-create'),
          data,
          format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

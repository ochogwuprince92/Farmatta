from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser

class UserTests(APITestCase):

    def test_register_user(self):
        url = '/users/api/register/'  # Update with the correct endpoint
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'is_farmer': True,
            'address': 'Test Address, City',
            'phone_number': '1234567890',
        }
        
        # Sending POST request to register
        response = self.client.post(url, data, format='json')
        
        # Assert that registration was successful (201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

        # Check if user was created in the database
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_farmer)

class UserTests(APITestCase):

    def setUp(self):
        # Create a user for login test
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123',
            is_farmer=True,
            address='Test Address, City',
            phone_number='1234567890'
        )

    def test_login_user(self):
        url = '/users/api/token/'  # JWT token obtain URL
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        
        # Sending POST request to log in and obtain token
        response = self.client.post(url, data, format='json')
        
        # Assert that login was successful (200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        # Check if the access token and refresh token are present
        self.assertIsNotNone(response.data['access'])
        self.assertIsNotNone(response.data['refresh'])

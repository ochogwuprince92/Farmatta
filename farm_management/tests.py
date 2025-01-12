from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser  # Ensure you import CustomUser for the foreign key
from farm_management.models import Crop
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT

class CropTests(APITestCase):
    def setUp(self):
        # Create a test user to associate with crops
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        
        # Get JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)  # Extract the access token
        
        # Set the URL for the crop list endpoint
        self.url = reverse('crop-list-create')
        
    def authenticate(self):
        # Add the JWT token to the request headers for authentication
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    def test_create_crop(self):
        # Authenticate before making the request
        self.authenticate()
        
        # Prepare the data for creating a crop
        data = {
            'name': 'Rice',
            'growth_stage': 'Seedling',
            'health_status': 'Healthy',
            'farmer': self.user.id  # Link crop to the test user
        }
        
        # Make a POST request to create a crop
        response = self.client.post(self.url, data, format='json')
        
        # Assert the crop was successfully created (status 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Crop.objects.count(), 1)
        self.assertEqual(Crop.objects.get().name, 'Rice')
    
    def test_list_crops(self):
        # Authenticate before making the request
        self.authenticate()
        
        # Create a crop to list
        Crop.objects.create(
            name='Rice',
            growth_stage='Seedling',
            health_status='Healthy',
            farmer=self.user
        )
        
        # Make a GET request to list the crops
        response = self.client.get(self.url)
        
        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One crop should be listed
        
    def test_update_crop(self):
        # Authenticate before making the request
        self.authenticate()
        
        # Create a crop to update
        crop = Crop.objects.create(
            name='Rice',
            growth_stage='Seedling',
            health_status='Healthy',
            farmer=self.user
        )
        
        # Prepare the updated data
        updated_data = {
            'name': 'Updated Rice',
            'growth_stage': 'Mature',
            'health_status': 'Excellent',
            'farmer': self.user.id
        }
        
        # Make a PUT request to update the crop
        response = self.client.put(reverse('crop-detail', args=[crop.id]), updated_data, format='json')
        
        # Assert the crop was successfully updated (status 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        crop.refresh_from_db()  # Refresh the crop instance
        self.assertEqual(crop.name, 'Updated Rice')
    
    def test_retrieve_crop(self):
        # Authenticate before making the request
        self.authenticate()
        
        # Create a crop to retrieve
        crop = Crop.objects.create(
            name='Rice',
            growth_stage='Seedling',
            health_status='Healthy',
            farmer=self.user
        )
        
        # Make a GET request to retrieve the crop
        response = self.client.get(reverse('crop-detail', args=[crop.id]))
        
        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Rice')
    
    def test_delete_crop(self):
        # Authenticate before making the request
        self.authenticate()
        
        # Create a crop to delete
        crop = Crop.objects.create(
            name='Rice',
            growth_stage='Seedling',
            health_status='Healthy',
            farmer=self.user
        )
        
        # Make a DELETE request to delete the crop
        response = self.client.delete(reverse('crop-detail', args=[crop.id]))
        
        # Assert the crop was successfully deleted (status 204 No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Crop.objects.count(), 0)

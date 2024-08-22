from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Story

class StoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_story_success(self):
        response = self.client.post('/api/stories/', {
            'title': 'Test Story',
            'image': None  # If image is optional, you can pass None
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Story')

    def test_create_story_invalid_data(self):
        response = self.client.post('/api/stories/', {
            'title': ''  # Title should not be empty
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_story(self):
        story = Story.objects.create(title='Test Story')
        response = self.client.get(f'/api/stories/{story.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Story')

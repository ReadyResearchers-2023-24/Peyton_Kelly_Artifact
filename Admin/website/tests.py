from django.test import TestCase

# Create your tests here.
# myapp/tests/test_views.py

import os
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Record
from .forms import SignUpForm, AddRecordForm

class ViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test record
        self.record = Record.objects.create(title='Test Record', file='test_file.txt')

        # Create a test client
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logging out

    def test_register_user_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Test registration with valid data
        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful registration

    # Add similar tests for other views like customer_record, delete_record, add_record, etc.

    def test_customer_record_view(self):
        # Ensure user is redirected to login page if not authenticated
        response = self.client.get(reverse('customer_record', kwargs={'pk': self.record.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test accessing customer_record with authenticated user
        response = self.client.get(reverse('customer_record', kwargs={'pk': self.record.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'record.html')

    # Add similar tests for delete_record, add_record, edit_record, upload, etc.

    def tearDown(self):
        # Clean up files after tests
        for filename in os.listdir("media/"):
            if filename == self.record.file:
                os.remove("media/uploads/" + filename)

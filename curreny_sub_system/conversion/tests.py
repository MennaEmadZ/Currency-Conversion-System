from django.urls import reverse
from rest_framework import status
import json
from unittest.mock import patch
from .views import get_latest_exchange_rate
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIClient
from .views import HistoryAPIView
from .models import CurrencyConversion
from .serializers import CurrencyConversionSerializer

# class CurrencyConversionAPITest(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.currency_conversion_url = reverse('currency-conversions') 
#         self.token_url = reverse('token_obtain_pair')  

#     def get_access_token(self):
        
#         payload = {
#             'username': 'mennae',
#             'password': 'mennaemad1234'
#         }
#         response = self.client.get(self.token_url, payload)
#         return response.data['access']
    
#     @patch('conversion.get_latest_exchange_rate')  
#     def test_currency_conversion_api(self, mock_get_latest_exchange_rate):
      
#         mock_get_latest_exchange_rate.return_value = 1.5 

#         # Get the access token
#         access_token = self.get_access_token()

#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

#         # Payload for the currency conversion request
#         payload = {
#             'from_currency': 'USD',
#             'to_currency': 'EUR',
#             'amount': 100
#         }

#         # Send POST request to the API
#         response = self.client.post(self.currency_conversion_url, payload, format='json')

#         # Verify the response
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn('amount', response.data) 


class HistoryAPIViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create some test data
        CurrencyConversion.objects.create(user=self.user, from_currency= 'USD',
            to_currency= 'EUR',
            amount= 120)
        CurrencyConversion.objects.create(user=self.user, from_currency= 'EGP',
            to_currency= 'USD',
            amount= 43)
        
        # Set up the request factory
        self.factory = RequestFactory()

    def test_history_with_authenticated_user(self):
        request = self.factory.get('currency/history/')
        force_authenticate(request, user=self.user)
        response = HistoryAPIView.as_view()(request)

        # Check response status
        self.assertEqual(response.status_code, 201)
        
        # Check the response data
        expected_data = CurrencyConversionSerializer(CurrencyConversion.objects.filter(user=self.user), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_history_with_unauthenticated_user(self):
        request = self.factory.get('currency/history/')
        response = HistoryAPIView.as_view()(request)

        # Check response status
        self.assertEqual(response.status_code, 401)

        # Check the response data
        self.assertEqual(response.data, {'error': 'User not authenticated.'})
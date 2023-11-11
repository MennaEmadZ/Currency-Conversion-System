from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversion
from .serializers import ConversionSerializer
from forex_python.converter import CurrencyRates
import datetime

class CurrencyConversionAPIView(APIView):
    def post(self, request, format=None):
        serializer = ConversionSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            source_currency = serializer.validated_data['from_currency']
            target_currency = serializer.validated_data['to_currency']
            source_amount = serializer.validated_data['amount']

            # Use forex-python to fetch real-time exchange rate and perform conversion
            c = CurrencyRates()
            # target_amount = c.convert(source_currency, target_currency,source_amount)
            conversion_rate = c.get_rate(source_currency, target_currency)

            target_amount = source_amount * conversion_rate

            # Save the conversion result in the database
            Conversion.objects.create(
                user = user,
                from_currency = source_currency,
                to_currency = target_currency,
                amount = target_amount,
                conversion_rate = conversion_rate,
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                is_permenant = False
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

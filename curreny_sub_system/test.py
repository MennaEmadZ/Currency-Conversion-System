from forex_python.converter import CurrencyRates
import requests

def get_latest_exchange_rate(source_currency, target_currency):
    # Use forex-python to fetch real-time exchange rate and perform conversion
    response = requests.get(f"https://v6.exchangerate-api.com/v6/479d6ca66f937907fee55fc3/pair/{source_currency}/{target_currency}") 
    
    return  response.json()



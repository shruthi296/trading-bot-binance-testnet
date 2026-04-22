from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # Fix timestamp issue
    client.TIME_OFFSET = client.get_server_time()['serverTime'] - int(time.time() * 1000)

    return client

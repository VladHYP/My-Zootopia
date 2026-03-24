import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetch the animals data for the animal 'animal_name'.
    Returns a list of animals.
    """
    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "name": animal_name
    }

    response = requests.get(API_URL, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
    
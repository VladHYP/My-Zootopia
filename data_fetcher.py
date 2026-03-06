import requests

API_KEY = "dcFkQi5UeOaNzyvXthvFiu1SLS1XBccDnzb4wM5N"
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "name": animal_name
    }

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
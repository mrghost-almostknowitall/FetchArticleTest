import requests
import os
from urllib.parse import unquote

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generateRandomImage(queryWord):
    UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
    orientation = "squarish"
    # decoded_url = unquote(url)
    # print(decoded_url)
    # url = "https://api.unsplash.com/photos/random?query=" + query + orientation + "&client_id=" + UNSPLASH_ACCESS_KEY

    url = f"https://api.unsplash.com/photos/random?query={queryWord}&orientation={orientation}&client_id={UNSPLASH_ACCESS_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        responseBody = response.json()
        print("Response Body:", responseBody)  # Print the response body for debugging

        if isinstance(responseBody, list):
            jsonObject = responseBody[0]
        else:
            jsonObject = responseBody

        imageUrl = jsonObject["urls"]["regular"]

        return imageUrl
    except Exception as e:
        print(e)
        return None
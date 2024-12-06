import requests
import json

API_URL = "https://ulvis.net/API/write/get"


def generateShortenURL(longURL, isPrivate, expireDate):
    completeURL = "https://edition.cnn.com" + longURL

    queryParams = ""
    if expireDate:
        queryParams = f"url={completeURL}&private={isPrivate}&expire={expireDate}"
    else:
        queryParams = f"url={completeURL}&private={isPrivate}"

    requestUrl = API_URL + "?" + queryParams

    response = requests.get(requestUrl)
    shortenedUrl = "NA"

    try:
        responseBody = response.text
        jsonObject = json.loads(responseBody)

        successRes = jsonObject["success"]

        if not successRes:
            raise Exception("Unexpected code " + str(response.status_code))

        if "data" in jsonObject:
            dataObject = jsonObject["data"]
            shortenedUrl = dataObject["url"]
            print("Shortened URL:", shortenedUrl)
        else:
            print("Error: 'data' field not found in the response.")
    except Exception as e:
        print(e)

    return shortenedUrl
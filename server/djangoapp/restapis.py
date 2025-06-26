# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="https://knittala-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="https://sentianalyzer.1x4k1nm78pii.us-south.codeengine.appdomain.cloud/analyze/Fantastic%20services")

def get_request(endpoint, **kwargs):
  #Add code for get requests to back end
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"
    request_url = backend_url+endpoint+"?"+params
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print("📥 Response JSON:", response.json())
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    import urllib.parse
    safe_text = urllib.parse.quote(text)
    request_url = sentiment_analyzer_url + "/" + urllib.parse.quote(text)

    print("Sentiment request URL:", request_url)

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        print("Sentiment raw response:", response.text)
        return response.json()
    except Exception as err:
        print(f"❌ Network error: {err}")
        return {'sentiment': 'neutral'}



# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print("✅ Review Post Response:", response.json())
        return response.json()
    except Exception as e:
        print("❌ Error:", e)
        return {"status": "error"}

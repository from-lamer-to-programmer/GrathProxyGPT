import requests
from dotenv import load_dotenv
import os

load_dotenv()
# Set up your proxy from .env
proxy = {
    'http': os.getenv("HTTP_PROXY"),
    'https': os.getenv("HTTPS_PROXY")
}

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Define the API endpoint URL
url = 'https://api.openai.com/v1/chat/completions'

# Set your request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}


def chatgpt(req):
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": req}
        ]
    }

    gptresponse = requests.post(url, headers=headers, json=data, proxies=proxy)
    return gptresponse.json()['choices'][0]['message']['content']

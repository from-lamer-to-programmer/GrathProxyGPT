import requests

# Set up your proxy details
proxy = {
    'http': 'http://truleridge_gmail_com:3ff5d0e6e1@45.135.12.218:30036',
    'https': 'http://truleridge_gmail_com:3ff5d0e6e1@45.135.12.218:30036'
}

# Set your OpenAI API key
api_key = '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'

# Define the API endpoint URL
url = 'https://api.openai.com/v1/chat/completions'

# Set your request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

# Set the payload for your request


# Make the request using the proxy



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


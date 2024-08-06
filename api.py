import requests

response = requests.get("https://fcsapi.com/api-v3/forex/latest?symbol=all_forex&access_key=hJ1KDJlOBqDfprVQbtJNhHOS")

print(response)

print(response.json())
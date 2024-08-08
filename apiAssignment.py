import requests

response = requests.get("https://fcsapi.com/api-v3/forex/latest?symbol=all_forex&access_key=hJ1KDJlOBqDfprVQbtJNhHOS")

data = response.json()

user_input = input("Enter a currency symbol: ").upper()

rates = data["response"]

filtered_user_input = [m for m in rates if user_input in m["s"]]

with open(f"{user_input}rates.txt", "a") as f:
    for s in filtered_user_input:
        f.write(f"{s['s']} - Rate: {s['c']}\n")

print(f"Exchange rates for {user_input} have been written to {user_input}rates.txt")

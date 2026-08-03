import requests

url = "https://www.shadowfox.in/"

print("Connecting to website...")

response = requests.get(url)

print("Connection Successful!")
print("Status Code:", response.status_code)
print("\nFirst 500 characters of the HTML:\n")
print(response.text[:500])
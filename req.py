import requests

one = "google."
two = "com"

response = requests.get(one + two)
print(response.status_code)

import requests

r = requests.get("https://www.dahliagreenevents.com")
print(r.status_code)
print(r.ok)
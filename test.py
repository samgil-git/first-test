##a small test as i learn git

import requests

r = requests.get("https://www.dahliagreenevents.com")
print(r.status_code)
print(r.ok)

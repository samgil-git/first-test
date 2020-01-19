import sys
import requests
import os
import math

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))
r = requests.get("https://www.dahliagreenevents.com")
print(r.status_code)

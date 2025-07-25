import requests

try:
    res = requests.get("http://server-container:8000")
    print("Response from server:", res.text)
except Exception as e:
    print("Failed to connect:", e)

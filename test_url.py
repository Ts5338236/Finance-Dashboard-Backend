import urllib.request
import urllib.error

url = 'http://127.0.0.1:8001/admin/'
try:
    with urllib.request.urlopen(url) as response:
        print(f"Status: {response.getcode()}")
        print(f"Body: {response.read().decode('utf-8')[:500]}")
except urllib.error.HTTPError as e:
    print(f"Status: {e.code}")
    print(f"Body: {e.read().decode('utf-8')}")
except Exception as e:
    print(e)

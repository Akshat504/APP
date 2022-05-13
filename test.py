import requests

url = 'http://localhost:5000/login'

data = {
    "uname": "akshat"
}

r = requests.post(url, data)
# r = requests.post(url)
print(r.content)




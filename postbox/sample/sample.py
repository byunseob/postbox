import requests

url = "http://localhost:3000/mail"
files = {'file': open('file.txt', 'rb')}
values = {
    "to": ["test@gmail.com", "test2@gmail.com"],
    "cc": ["test@gmail.com", "test2@gmail.com"],
    "subject": "title",
    "content": "<h1>hi</h1>",
    "alias": "byunseob",
    "content_type": "html"
}

r = requests.post(url, files=files, data=values)

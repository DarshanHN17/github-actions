import requests

print("hi")
output=requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(output.json())

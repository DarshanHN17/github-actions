import requests

print("Hello World")
output=requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(output.json())

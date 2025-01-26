import requests

base_url = 'http://127.0.0.1:8080'

with open('test_image.png', 'rb') as file:
    files = {'image': file}

    response_post = requests.post(f'{base_url}/upload', files=files)
print(response_post.text)

response_get = requests.get(f'{base_url}/image/test_image.png', headers={'Content-Type': 'text'})
print(response_get.text)

response_delete = requests.delete(f'{base_url}/delete/test_image.png')
print(response_delete.text)

"""
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi
у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi. Серед цих
даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових
запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests
"""

import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
parameters = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
resp = requests.get(url, params=parameters)

response_data = resp.json()

counter = 0
image_links = []
for answer in response_data.get('photos'):
    image_links.append(response_data.get('photos')[counter].get('img_src'))
    counter += 1

print(image_links)
try:
    pic_num = 1
    for link in image_links:
        with open(f'mars_photo{pic_num}.jpg', 'wb') as f:
            f.write(requests.get(link).content)
            pic_num += 1

except Exception as e:
    print(f'Process ended with error {e}')

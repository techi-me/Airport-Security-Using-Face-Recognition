import requests
import base64
import json

image_path="face-2.4.jpg"
image = open(image_path, 'rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read)
url="http://127.0.0.1:8000/laser_security/get_image"
data = {'image':image_64_encode}
headers = {
   'content-type': "multipart/form-data",
   'accept': "application/json"
}

r = requests.post(url, data=data)
print(r.text)

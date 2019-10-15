import requests, os, sys

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')
image_path = sys.argv[1]

url = 'http://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

print(response.text)

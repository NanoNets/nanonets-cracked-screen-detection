import requests, os

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

url = 'http://app.nanonets.com/api/v2/ImageCategorization/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")
import requests, os, json

url = "http://app.nanonets.com/api/v2/ImageCategorization/Model/"
api_key = os.environ.get('NANONETS_API_KEY')

payload = {'categories' : ["mobile-damaged", "mobile-not-damaged"]}
headers = {'accept': "application/x-www-form-urlencoded",}

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''), data=payload)
print(response.text)
model_id = json.loads(response.text)["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")

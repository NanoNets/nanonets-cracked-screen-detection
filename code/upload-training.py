import os, requests

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

batch_size=20

damaged_dir = './data/mobile_damaged/'
not_damaged_dir = './data/mobile_not_damaged/'
damaged_files = [damaged_dir + x for x in os.listdir(damaged_dir)]
not_damaged_files = [not_damaged_dir + x for x in os.listdir(not_damaged_dir)]
all_files = [damaged_files, not_damaged_files]
categories = ["mobile-damaged", "mobile-not-damaged"]

train_dict = dict(zip(categories, all_files))

for category in categories:
        print('Uploading for category: ', category)
        batch_nb = 1
        files = train_dict[category]
        if len(files)%batch_size == 0:
                total_batches = int(len(files)/batch_size)
        else:
                total_batches = int(int(len(files)/batch_size) + 1)
        url = 'https://app.nanonets.com/api/v2/ImageCategorization/UploadFile/?modelId=%s&category=%s'%(model_id, category)             
        while len(train_dict[category]) > 0:
                multiple_files = []
                batch_images, train_dict[category] = train_dict[category][:batch_size], train_dict[category][batch_size:]
                print('Batch {}/{} of images'.format(batch_nb, total_batches))                          
                for image in batch_images:
                        image_name = image.split('/')[-1]
                        multiple_files.append(('file', (image_name, open(image, 'rb'), 'image/jpeg')))
                response = requests.post(url, 
                                         auth=requests.auth.HTTPBasicAuth(api_key, ''), 
                                         files=multiple_files)
                batch_nb+=1

print("\n\n\nNEXT RUN: python ./code/train-model.py")

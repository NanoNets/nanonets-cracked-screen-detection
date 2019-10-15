<div align="center">
  <a href="https://nanonets.com/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets Cracked Screen Detection Python Sample" width="100"/>
    </a>
</div>

<h1 align="center">NanoNets Cracked Screen Detection Python Sample</h1>

** **

## Cracked Screen Detection

We will use the Nanonets Image Classification API to determine from a picture of a phone whether it is damaged or not. 

>**Note:** Make sure you have python and pip installed on your system if you don't visit
[Python](https://www.python.org/downloads/release/python-2714/), 
[pip](https://pip.pypa.io/en/stable/installing/)


### Step 1: Clone the Repo, Install dependencies
```bash
git clone https://github.com/NanoNets/nanonets-cracked-screen-detection.git
cd nanonets-cracked-screen-detection
sudo pip install requests tqdm
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/#/keys

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create-model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in the ```data``` directory
```bash
python ./code/upload-training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train-model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model-state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./data/mobile_damaged/00000028.jpg
```


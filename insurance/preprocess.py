# %%
import os
import pandas as pd

from dkube.sdk import *

import warnings
warnings.filterwarnings("ignore")
import requests, argparse
requests.packages.urllib3.disable_warnings()

# %% [markdown]
# ### Set up the variables for Dataset Access

# %%
MLFLOW_EXPERIMENT_NAME = os.getenv('DKUBE_PROJECT_NAME')

## Get the username & token and create the DKube SDK API variables

SERVING_DKUBE_URL = os.environ.get("DKUBE_URL")
SERVING_DKUBE_TOKEN = os.environ.get("DKUBE_USER_ACCESS_TOKEN")
SERVING_DKUBE_USERNAME = os.environ.get("DKUBE_USER_LOGIN_NAME")
SERVING_DKUBE_PROJECT_ID = os.environ.get("DKUBE_PROJECT_ID")

SERVING_DKUBE_INPUT_DATASET_NAME = "insurance-input-dataset"
SERVING_DKUBE_OUTPUT_DATASET_NAME = "insurance-output-dataset"

dapi = DkubeApi(URL=SERVING_DKUBE_URL,token=SERVING_DKUBE_TOKEN)
dataset_input_info = DkubeDataset(SERVING_DKUBE_USERNAME, name=SERVING_DKUBE_INPUT_DATASET_NAME)
dataset_output_info = DkubeDataset(SERVING_DKUBE_USERNAME, name=SERVING_DKUBE_OUTPUT_DATASET_NAME)

# %% [markdown]
# ### Preprocess Data

# %%
## Get the original data from the input dataset repo mount point & write to output dataset
data = pd.read_csv('/input/dataset/insurance.csv')
# dapi.create_dataset(dataset_output_info)

## Remove the AGE column & write out the new output dataset
insurance_filtered = data.drop('age', axis=1)
insurance_filtered.to_csv('/output/dataset/insurance.csv')



#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from dkube.sdk import *

import warnings
warnings.filterwarnings("ignore")
import requests, argparse
requests.packages.urllib3.disable_warnings()

# Set up the variables for Dataset Access

SERVING_DKUBE_URL = os.environ.get("DKUBE_URL")
SERVING_DKUBE_TOKEN = os.environ.get("DKUBE_USER_ACCESS_TOKEN")
SERVING_DKUBE_USERNAME = os.environ.get("DKUBE_USER_LOGIN_NAME")
SERVING_DKUBE_PROJECT_ID = os.environ.get("DKUBE_PROJECT_ID")

DATASET_INPUT_DIR = "/input/dataset/"
DATASET_OUTPUT_DIR = "/output/dataset/"

dapi = DkubeApi(URL=SERVING_DKUBE_URL,token=SERVING_DKUBE_TOKEN)
dataset_input_info = DkubeDataset(SERVING_DKUBE_USERNAME, name=SERVING_DKUBE_INPUT_DATASET_NAME)
dataset_output_info = DkubeDataset(SERVING_DKUBE_USERNAME, name=SERVING_DKUBE_OUTPUT_DATASET_NAME)

# Preprocess Data

## Get the original data from the input dataset repo mount point & write to output dataset
data = pd.read_csv(DATASET_INPUT_DIR + 'insurance.csv')

## Remove the AGE column & write out the new output dataset
insurance_filtered = data.drop('age', axis=1)
insurance_filtered.to_csv(DATASET_OUTPUT_DIR + 'insurance.csv')

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:59:33 2022

@author: Max_l
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "isS3P7auiIh4rzYJVtIMforGUPRhkBUhxz1GPVFJ_MbV"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['cylinders','displacement','horsepower','weight','model year','origin']],
                                   "values": [[8,307,130,3504,70,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/947e6ad9-2c7b-4002-9bdf-5e10aac95859/predictions?version=2022-11-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
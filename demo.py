import os
import pandas as pd
from openai import OpenAI
import requests
import json
from datetime import datetime


df = pd.read_csv('jobs_ok.csv')
print(f"Nbr of rows: {len(df)}")
#df.head()

# Set var env from ollama:
# os.environ["OPENAI_API_KEY"] = "ollama"
# os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1/"

# system_message = """I would you act as a helpful assisstant. Your role is read carefully the instructions given by the user, then process the input data, and finally output a data based on your understanting of the instructions.
# Please follow exactly the instructions provided by the user and answer as accurate as possible.
# Please ensure that your responses are technically unbiased. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
# If you don't know the answer to a question, please don't share false information and ask the user for clarification if required.
# Please be brief and do not add any additional explanations or clarifications."""

# prompt = """In order to build a database of jobs, we collected a list of jobs from different websites and we need you to help us classifying these jobs.
# Your task is to generate most popular job classification methods using two type of measures: Category, Industry"""

# MODEL_NAME = "llama3.1"

# client = OpenAI(
#     api_key = os.environ["OPENAI_API_KEY"],
#     base_url = os.environ["OPENAI_BASE_URL"]
# )

# system_message = """I would you act as a helpful assisstant. Your role is read carefully the instructions given by the user, then process the input data, and finally output a data based on your understanting of the instructions.
# Please follow exactly the instructions provided by the user and answer as accurate as possible.
# Please ensure that your responses are technically unbiased. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
# If you don't know the answer to a question, please don't share false information and ask the user for clarification if required.
# Please be brief and do not add any additional explanations or clarifications."""

# prompt = """In order to build a database of jobs, we collected a list of jobs from different websites and we need you to help us classifying these jobs.
# Your task is to generate most popular job classification methods using two type of measures: Category, Industry"""

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": system_message,
#         },
#         {
#             "role": "user",
#             "content": prompt,
#         }
#     ],
#     model = MODEL_NAME,
#     # temperature=0.7,
#     # max_tokens=500,
# )

# print(chat_completion.choices[0].message.content)

# API endpoint URL
api_url = os.environ['GITPOD_WORKSPACE_URL']

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # Replace with your actual access token if required
}

# Function to convert DataFrame row to Job model dictionary
def row_to_job_dict(row):
    return {
        'title': row['title'],
        'description': row['description'],
        'likeCount': int(row['likeCount']),
        'price': float(row['price']),
        'pricePreview': row['pricePreview'],
        'priceType': row['priceType'],
        'priceUnit': row['priceUnit'],
        'quantity': int(row['quantity']),
        'status': row['status'],
        'category': row['category'],
        # 'specs': json.loads(row['specs']) if pd.notna(row['specs']) else None,
        'city': row['city'],
        'region': row['region']
    }

# Iterate through the DataFrame and send POST requests
for index, row in df.iterrows():
    job_data = row_to_job_dict(row)
    
    try:
        response = requests.post(api_url, json=job_data, headers=headers)
        response.raise_for_status()
        print(f"Job {index + 1} inserted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error inserting job {index + 1}: {e}")

print("Job insertion process completed.")

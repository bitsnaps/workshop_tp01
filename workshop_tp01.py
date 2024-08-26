
import os
import time
import regex as re # Unicode support
import requests
import numpy as np
import pandas as pd
from openai import OpenAI

df = pd.read_csv('jobs_ok.csv')
print(len(df))
df.head()

# Set var env from ollama:
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434"

system_message = """I would you act as a helpful assisstant. Your role is read carefully the instructions given by the user, then process the input data, and finally output a data based on your understanting of the instructions.
Please follow exactly the instructions provided by the user and answer as accurate as possible.
Please ensure that your responses are technically unbiased. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
If you don't know the answer to a question, please don't share false information and ask the user for clarification if required.
Please be brief and do not add any additional explanations or clarifications."""

prompt = """In order to build a database of jobs, we collected a list of jobs from different websites and we need you to help us classifying these jobs.
Your task is to generate most popular job classification methods using two type of measures: Category, Industry"""

MODEL_NAME = "llama3"

client = OpenAI(
    api_key = os.environ["OPENAI_API_KEY"],
    base_url = os.environ["OPENAI_BASE_URL"]
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model = MODEL_NAME,
    # temperature=0.7,
    # max_tokens=500,
)

print(chat_completion.choices[0].message.content)
# The goal is to ask ChatGPT to summarize class responses

import os

import pandas as pd
import openai

embed_model = 'gpt-4-0314'
openai.api_key = os.getenv('OPENAI_API_KEY')


df = pd.read_csv("/home/taiphoon/Downloads/"
                 "Survey1 Quiz Student Analysis Report.csv")

df.columns
desired_col = [c for c in df.columns if c.find('problems') >= 0][0]
resp = df[desired_col]

prompt = ("Please summarize the following responses into the topics and "
          "the number of responses that mention the topic. Please assume "
          "each response is separted by the symbol:\n\n |||")

user_message = prompt + '|||'.join(resp)
user_message

summ = openai.ChatCompletion.create(
    model=embed_model,
    messages=[
        {'role': 'system', 'content': 'You are an executive assistant'},
        {'role': 'user', 'content': user_message}])

summ.keys()
assert len(summ['choices']) == 1
print(summ['choices'][0]['message']['content'])

# The goal is to summarize student responses into a list

import re
import logging
import os
from pathlib import Path

import pandas as pd
import torch
import transformers

logging.basicConfig(level=logging.INFO,
                    format=('%(asctime)s - %(name)s - %(levelname)s'
                            ' - %(message)s'),
                    filename='collapse.log')

# Local copy of Llama3
MODEL_ID = '/home/wtailee/repos/Meta-Llama-3-8B-Instruct'

pipeline = transformers.pipeline(
  "text-generation",
  model=MODEL_ID,
  model_kwargs={"torch_dtype": torch.bfloat16},
  device_map="auto"
  )

TERM_TOKEN = "<|eot_id|>"
terminators = [
  pipeline.tokenizer.eos_token_id,
  pipeline.tokenizer.convert_tokens_to_ids(TERM_TOKEN)
  ]


def format_prompt(prompt, role='user'):
    """Formats prompt into Llama format with roles"""
    assert isinstance(prompt, str)
    formatted_prompt = [
      {'role': role,
       'content': prompt}]
    return formatted_prompt


stud_input = pd.read_csv(
  "/home/wtailee/Downloads/"
  "Survey 1 Survey Student Analysis Report.csv")
q_cols = [col for col in stud_input.columns if re.search('^[0-9]{7}', col)]

col = q_cols[0]
prompt = ('I asked the class this question: """' + re.sub('^[0-9: ]+', '', col)
          + '"""\nBelow are the responses from students, please categorize '
          'each response into topics like finance, sports, AI, etc. Then report, for each '
          'student, what topics were in their answer. It is '
          'possible to have multiple or no topics matching their answer.\n\n'
          + '\n  -- '.join(stud_input[col].to_numpy()))
prompt = ('I asked the class this question: """' + re.sub('^[0-9: ]+', '', col)
          + '"""\nBelow are the responses from students, please categorize '
          'each response into topics like finance, sports, AI, etc then report,'
          'the top 3 popular topics and their frequency. It is '
          'possible to have multiple or no topics matching their answer.\n\n'
          + '\n  -- '.join(stud_input[col].to_numpy()))

thread = format_prompt(
  'You are a college professor who is helping the user organize and sharpen their thoughts.', 'system')

thread.extend(format_prompt(prompt))
prompt_tok = pipeline.tokenizer.apply_chat_template(
  thread,
  tokenize=False,
  max_new_tokens=100)

outputs = pipeline(
  prompt_tok,
  eos_token_id=terminators,
  top_k=1)

answer = outputs[0]['generated_text'].split(f'{term_token}assistant')[-1].strip()
print(answer)

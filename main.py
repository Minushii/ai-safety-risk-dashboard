""" pip install pandas -> 
                openpyxl ->library in Python is a powerful tool for reading, writing, and modifying Excel 2010 and later files
                matplotlib -> visualization in python 
                seaborn -> used for creating graphics

"""

import pandas as pd
from pipeline.decomposition import decompose_prompt
from pipeline.stepExecution import step_execution

from fastapi import FastAPI

# using pydantic library to define what type of text should be sent to the API
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt:str

app = FastAPI()
@app.get("/")
def home():
    return "Hello from FastAPI!"

@app.post("/analyze")
def analyze(request:PromptRequest):
    result = decompose_prompt(request.prompt)
    return result

# #load the prompts 
# prompts = pd.read_csv("data/harmful_behaviors.csv")

# #preview first 5 rows
# print(prompts.head())

# #Basic infor
# print(prompts.info())

# #check how many missing vlaues are there in each column 
# print(prompts.isnull().sum())



# answers_from_llm = step_execution(result)
# print(answers_from_llm)

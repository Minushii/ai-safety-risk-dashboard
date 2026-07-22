""" pip install pandas -> 
                openpyxl ->library in Python is a powerful tool for reading, writing, and modifying Excel 2010 and later files
                matplotlib -> visualization in python 
                seaborn -> used for creating graphics

"""

import pandas as pd
from pipeline.decomposition import decompose_prompt
from pipeline.stepExecution import step_execution

# #load the prompts 
# prompts = pd.read_csv("data/harmful_behaviors.csv")

# #preview first 5 rows
# print(prompts.head())

# #Basic infor
# print(prompts.info())

# #check how many missing vlaues are there in each column 
# print(prompts.isnull().sum())

userPrompt = input("Enter your prompt: ")
result = decompose_prompt(userPrompt)
answers_from_llm = step_execution(result)
print(answers_from_llm)

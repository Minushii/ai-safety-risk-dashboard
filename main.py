""" pip install pandas -> 
                openpyxl ->library in Python is a powerful tool for reading, writing, and modifying Excel 2010 and later files
                matplotlib -> visualization in python 
                seaborn -> used for creating graphics

"""

import pandas as pd

#load the prompts 
prompts = pd.read_csv("data/harmful_behaviors.csv")

#preview first 5 rows
print(prompts.head())

#Basic infor
print(prompts.info())
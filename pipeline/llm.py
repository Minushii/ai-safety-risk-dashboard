#the llm will generate the response for each step
import requests
import json
import os



def generate_response(prompt):

    api_key = os.getenv("FIREWORKS_API_KEY")
    

    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    payload = {
    "model": "accounts/fireworks/models/gpt-oss-120b",
    "max_tokens": 1000,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.6,
    "messages": [
        {
        "role": "user",
        "content": prompt
        }
    ]
    }
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    #get reponse object
    #requests is a python tool that sends HTTP requests to a server using the info that you give 
    #(like the url the boady and the header) and get you a response from the server

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    
    #the response you get is a json becuase most llms return json 
    #convert it to a python dectionary 
    data = response.json()

    #in order to get the output from the dictionary detect where the content is 
    # print(response.status_code)
    print(data)
    text = data["choices"][0]["message"]["content"]
    return text
    
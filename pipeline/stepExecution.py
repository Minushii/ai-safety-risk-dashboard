#This script will take in the COT prompts each one by one will be taken and then sent to an llm 
#at the moment the llm will be hardcoded 
#Future improvements: the user gets to choose the llm 
from pipeline.llm import generate_response

def step_execution(decomposed_steps):
    #the input given is in json format step: prompt:
    """1. Take the prompt part from the dictionary
       2. send the prompt to the gnereate response function
       3. store the answer 
       4. repeat it for all the prompts
       5. return the answers"""

    for step in decomposed_steps:
        stepPrompt = step["prompt"]
        answerPrompt = f"You are a research assistant. Answer clearly and descriptively {stepPrompt}"
        answerFromLlm = generate_response(answerPrompt)
        step["answer"] = answerFromLlm
    return decomposed_steps
    



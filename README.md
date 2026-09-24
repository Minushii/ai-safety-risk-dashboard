# AI Safety Risk Analysis

## About
This project is built around the idea of my Master's minor thesis, titled "Investigating Chain-of-Thought Jailbreaks: A Study of Masked and Unmasked Reasoning in Large Language Models."
The idea behind the research was to understand how an LLM behaves when it is given a harmful prompt indirectly. LLMs are generally trained to avoid directly answering harmful requests, but what happens if a harmful request is broken down into smaller questions that appear harmless on their own?
For example, instead of directly asking an LLM for something harmful, the original request can be broken down into a series of smaller and seemingly harmless questions that gradually lead towards the original request.
A human can think about a problem step by step to reach a final goal. This project builds around that idea by breaking a given prompt down into smaller steps and using an LLM to work through those steps.
The project then evaluates the LLM's responses at each step to understand whether the model maintains its safety behaviour throughout the process or produces a harmful response at any point. 

## Version 1
Version 1 is a simple prototype of this idea.

The current system:
    Takes a user prompt.
    Uses an LLM to decompose the prompt into smaller steps.
    Uses an LLM to generate an answer for each step.
    Uses a separate/or same LLM as a judge to evaluate the generated answer.
    Displays the results through a React interface.

The judge currently evaluates the generated responses for:
    Harmfulness
    Severity
    Categories
    Confidence
    Refusal behaviour

## Tech Stack
Python, FastAPI, React, Fireworks AI

## Project Structure
AI SAFETY RISK ANALYSIS 
    - fronend/
    - pipeline/
        - decompostion.py
        - llm.py
        - scoring.py
        - stepExecution.py
    - main

Backend
    * main.py — FastAPI application. Receives the prompt from the frontend and connects the request to the Python pipeline.
    * pipeline/llm.py — Handles communication with the Fireworks AI API.
    * pipeline/decomposition.py — Sends the prompt to the LLM and breaks it down into smaller steps.
    * pipeline/stepExecution.py — Sends each decomposed step to the LLM and collects the generated responses.
    * pipeline/scoring.py — Uses a separate LLM to evaluate the generated responses for safety.

Frontend
    * frontend/ — Contains the React application and user interface.

## Requirements
Before running the project, you will need:
    Python 3.10+
    Node.js and npm
    A Fireworks AI API key
The backend uses Python and FastAPI, while the frontend is built with React and Vite.


## How It Works
Brief explanation of the pipeline.

## Future Improvements
What you plan to add later.
import os
from dotenv import load_dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# accessToken from https://chat.openai.com/api/auth/session
llm = GPT4OpenAI(token=os.environ["OPENAI_ACCESS_TOKEN"], model='gpt-4-browsing')
# ChatGPT will first browse the web for the name/age of her boyfriend, then return the answer
response = llm('What is the age difference between Dua Lipa and her boyfriend?')

print(response)

"""
Expected answer:
The age difference between Dua Lipa and her boyfriend Romain Gavras is 14 years. As of 2023, Romain Gavras is 41 years old, while Dua Lipa is 27 years old【5†source】.
"""
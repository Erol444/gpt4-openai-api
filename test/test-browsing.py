import os
from dotenv import load_dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"], headless=False, model='gpt-4-browsing')
# ChatGPT will first browse the web for the name/age of her boyfriend, then return the answer
response = llm('What is the age difference between Dua Lipa and her boyfriend?')
print(response)

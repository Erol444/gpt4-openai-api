import os
from dotenv import load_dotenv # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"],
                 headless=False,
                 # Either "text-davinci-002-render-sha" (GPT-3.5), "gpt-4", "gpt-4-code-interpreter", or "gpt-4-plugins"
                 model='gpt-4-code-interpreter')

response = llm('What are all prime numbers between 1 and two hundred?')
print(response)

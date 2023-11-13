import os
from dotenv import load_dotenv  # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Since November 2023, browsing is integrated into the GPT-4

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"],
                 headless=False, model='gpt-4')

response = llm('What is the age difference between Dua Lipa and her boyfriend?')
print(response)

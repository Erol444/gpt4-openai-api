import os
from dotenv import load_dotenv # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"], headless=False, model='gpt-4')
# GPT3.5 will answer 8, while GPT4 should be smart enough to answer 10
response = llm('If there are 10 books in a room and I read 2, how many books are still in the room?')
print(response)

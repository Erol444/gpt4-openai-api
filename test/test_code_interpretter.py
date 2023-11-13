import os
from dotenv import load_dotenv # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Since November 2023, code interpretter is integrated into the GPT-4

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"],
                headless=True,
                # Either "text-davinci-002-render-sha" (GPT-3.5), "gpt-4", or "gpt-4-plugins"
                model='gpt-4')

response = llm('What are all prime numbers between 1 and 200?')
print(response)
llm.close()
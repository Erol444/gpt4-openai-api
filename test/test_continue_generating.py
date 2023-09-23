import os
from dotenv import load_dotenv # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"], model='gpt-4', auto_continue=True, headless=False)

prompt = """
Please write a detailed and comprehensive guide to developing a small business, starting from a business idea and
going through all the necessary steps, such as writing a business plan, choosing a legal structure, obtaining financing,
choosing a location, setting up your workspace, recruiting and hiring employees, developing products and services,
marketing, sales, customer service, accounting and bookkeeping, reviewing business performance, and finally planning for
growth and expansion. Be sure to include examples, tips, and potential pitfalls to watch out for along the way.
"""
response = llm(prompt)

# GPT4 should now return all 15 different steps of the business plan, one by one
print(response)

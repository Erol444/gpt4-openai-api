import os
from dotenv import load_dotenv
from gpt4_openai import GPT4OpenAI
load_dotenv()

# accessToken from https://chat.openai.com/api/auth/session
# Plugin IDs can be found here: https://github.com/acheong08/ChatGPT/blob/main/docs/plugins.json
llm = GPT4OpenAI(token=os.environ["OPENAI_ACCESS_TOKEN"],
                 model='gpt-4',
                 plugin_ids=['plugin-d1d6eb04-3375-40aa-940a-c2fc57ce0f51'] # Wolfram Alpha
                 )

# ChatGPT will use Wolfram Alpha plugin to calculate the equation
response = llm('Calculate the square root of 12345 to 10 decimal places')
print(response)

"""
Expected answer:

Calculating the square root of a number can be done using various methods, but for large numbers and precise decimal places, the best way is to use a calculator or programming tool.

Here's the square root of 12345 calculated to 10 decimal places:

√12345 = 111.1080555135
"""
from dotenv import load_dotenv # pip install python-dotenv
import os
from gpt4_openai import GPT4OpenAI
from langchain import LLMChain
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate)

load_dotenv()

template="You are a helpful assistant that translates english to pirate."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi")
example_ai = AIMessagePromptTemplate.from_template("Argh me mateys")
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"], headless=False)
chain = LLMChain(llm=llm, prompt=chat_prompt)
print(chain.run("My name is John and I like to eat pizza."))


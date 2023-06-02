# GPT4 OpenAI unofficial API

## Unofficial GPT-4 API access via chat.openai.com

Have you **applied to GPT-4 API access** but **OpenAI is too busy to reply**? Me too, that's why I created this package. If the account has `ChatGPT Plus`, you can use **GPT-4**.

It supports both **GPT4 browser and plugins** by selecting model via `GPT4OpenAI(token=token, model='gpt-4-browsing')`, or `model='gpt-4-plugins'`.

**Note:** This unofficial API library is not endorsed by OpenAI and violates their Terms of Service. Use it at your own risk; the creator assumes no liability for any consequences. Please adhere to platform's ToS and exercise caution with unofficial resources.

The core logic was taken from the [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT).

## Demo

![Demo GIF](https://user-images.githubusercontent.com/18037362/236707120-e93d40bc-b73b-4f72-bc7d-d0449a082946.gif)

## Demo script

```python
from gpt4_openai import GPT4OpenAI

# accessToken from https://chat.openai.com/api/auth/session
llm = GPT4OpenAI(token=my_token, model='gpt-4')
# GPT3.5 will answer 8, while GPT4 should be smart enough to answer 10
response = llm('If there are 10 books in a room and I read 2, how many books are still in the room?')
print(response)
```

As seen on the demo gif (above), GPT-4 answers correctly.

## Browsing support

```python
from gpt4_openai import GPT4OpenAI

# accessToken from https://chat.openai.com/api/auth/session
llm = GPT4OpenAI(token=my_token, model='gpt-4-browsing')
# ChatGPT will first browse the web for the name/age of her boyfriend, then return the answer
response = llm('What is the age difference between Dua Lipa and her boyfriend?')
print(response)
```

## Plugin support

List of plugin IDs can be [found here](https://github.com/acheong08/ChatGPT/blob/main/docs/plugins.json).

```python
llm = GPT4OpenAI(token=my_token, model='gpt-4',
                 plugin_ids=['plugin-d1d6eb04-3375-40aa-940a-c2fc57ce0f51'] # Wolfram Alpha
                 )

# ChatGPT will use Wolfram Alpha plugin to calculate the equation
response = llm('Calculate the square root of 12345 to 10 decimal places')
print(response)
```

## Langchain support

`GPT4OpenAI` actually extends `LLM` class from `langchain.llms.base`. So you can easily use this library inside langchain ecosystem. Example:

```python
from gpt4_openai import GPT4OpenAI
from langchain import LLMChain
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate)

template="You are a helpful assistant that translates english to pirate."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi")
example_ai = AIMessagePromptTemplate.from_template("Argh me mateys")
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])

# accessToken from https://chat.openai.com/api/auth/session
llm = GPT4OpenAI(token=my_token)

chain = LLMChain(llm=llm, prompt=chat_prompt)
print(chain.run("My name is John and I like to eat pizza."))
```

Output will be:
```
AI: Ahoy, me name be John an' I be likin' ta feast on some pizza, arr!
```

## How to get the access token

1. Go to https://chat.openai.com/api/auth/session
2. In the JSON, copy the whole `accessToken` field.

![image](https://github.com/Erol444/gpt4-openai-api/assets/18037362/c0bdfd9c-8ad1-48ca-8344-621a4513e04b)

## OpenAI's GPT4 vs other providers

Initially, I tried [poe.com ](https://poe.com/) (private API implemented at [gpt4free](https://github.com/gptforfree/gpt4free/tree/main/quora)), but noticed that input context window is smaller than one of OpenAI ChatGPT. And the same goes for Bing's GPT4.

## Installation

To install this Python package, run the following command:

```bash
pip install gpt4-openai-api
```

## Dependencies

These dependencies get downloaded directly:

- `revChatGPT` ([acheong08/ChatGPT](https://github.com/acheong08/ChatGPT))
- `langchain`

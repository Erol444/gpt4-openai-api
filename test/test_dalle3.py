import os
from dotenv import load_dotenv # pip install python-dotenv
from gpt4_openai import GPT4OpenAI
import cv2
import numpy as np
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"],
                headless=True,
                model='gpt-4' # DALL-E 3 only works with gpt-4
                )

bytes = llm.generate_image('Generate an isometric image of a cute doggo inside a house.', image_path = './optional_path.png')

# Convert image bytes to numpy array
img = cv2.imdecode(np.frombuffer(bytes, np.uint8), -1)
cv2.imshow('image', img)
cv2.waitKey(0)

llm.close()
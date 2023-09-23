from typing import Optional, List, Mapping, Any
from time import sleep

from langchain.llms.base import LLM

from .driver import ChatGptDriver

class GPT4OpenAI(LLM):

    history_data: Optional[List] = []
    token : Optional[str]
    chatbot : Optional[ChatGptDriver] = None
    call : int = 0
    conversation : Optional[str] = ""
    headless : bool = True
    __file__ = __file__
    model: str = "gpt-4"

    #### WARNING : for each api call this library will create a new chat on chat.openai.com
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            pass
            #raise ValueError("stop kwargs are not permitted.")
        #token is a must check
        if self.chatbot is None:
            if self.token is None:
                raise ValueError("Need a token , check https://chat.openai.com/api/auth/session for get your token")
            else:
                if self.conversation == "":
                    self.chatbot = ChatGptDriver(self.token, headless=self.headless, model=self.model)
                elif self.conversation != "" :
                    self.chatbot = ChatGptDriver(self.token, headless=self.headless, model=self.model, conversation_id=self.conversation)
                else:
                    raise ValueError("Something went wrong")

        response = ""
        # OpenAI: 50 requests / hour for each account
        if self.call >= 45:
            raise ValueError("You have reached the maximum number of requests per hour ! Help me to Improve. Abusing this tool is at your own risk")
        else:
            sleep(2)
            data = self.chatbot.send_message(prompt)
            #print(data)
            response = data["message"]
            self.conversation = data["conversation_id"]
            FullResponse = data
            self.call += 1

        #add to history
        self.history_data.append({"prompt":prompt,"response":response})

        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": self.model, "token": self.token}

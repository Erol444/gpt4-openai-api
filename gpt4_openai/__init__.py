from typing import Optional, List, Mapping, Any
from langchain.llms.base import LLM
from revChatGPT.V1 import Chatbot


class GPT4OpenAI(LLM):

    history_data: Optional[List] = []
    token : Optional[str]
    chatbot : Optional[Chatbot] = None
    call : int = 0
    conversation : Optional[str] = ""
    headless : bool = True
    __file__ = __file__
    model: str = "gpt-4"
    plugin_ids: List[str] = []
    auto_continue: bool = False

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if self.chatbot is None:
            if self.token is None:
                raise ValueError("You need to specify the token, please check https://github.com/Erol444/gpt4-openai-api#how-to-get-the-access-token")

            self.chatbot = Chatbot({
                'access_token': self.token,
                'model': self.model,
                'plugin_ids': self.plugin_ids
                })

        response = ""
        for data in self.chatbot.ask(prompt=prompt,
                                     auto_continue=self.auto_continue,
                                     model=self.model):
            response = data["message"]

        # Add to history
        self.history_data.append({"prompt":prompt,"response":response})

        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": self.model, "token": self.token}

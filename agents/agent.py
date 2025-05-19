import openai
from abc import ABC, abstractmethod
from loguru import logger
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class AgentBase(ABC):
    def __init__(self,name,max_retries=2,verbose=True): #name of the model, max number of retries to generate output from llm =2
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self,*args,**kwargs):
        pass

    def call_openai(self,messages,temparature=0.8,max_tokens=150):
        retries = 0
        while retries<self.max_retries:
            try:
                if self.verbose:
                    logger.name(f"[{self.name}] Sending message to OpenAI")

                    for msg in messages:
                        logger.debug(f" {msg['role']}: {msg['content']} ")
                
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,  
                    temperature=temparature,  
                    max_tokens=max_tokens
                )


                reply = response.choices[0].message

                if self.verbose:
                    logger.info(f"[{self.name}] Received Response: {reply}")
                
                return reply
            
            except Exception as e:
                retries +=1
                logger.error(f"[{self.name}] Error during OpenAI call maybe: {e}. Retry {retries}/{self.max_retries}")
            
        raise Exception("Error")


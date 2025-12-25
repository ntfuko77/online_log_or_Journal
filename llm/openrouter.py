from openai import OpenAI
from dotenv import load_dotenv 
# Third-party library
import os
from enum import Enum
import logging
load_dotenv()
from base_function_call_type import ResponseInput
class default_config(Enum):
    model="openai/gpt-oss-20b:free"
    



class OpenRouterClient:
    def __init__(self, api_key: str):

        api_key = os.getenv("OPENROUTER_API_KEY")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key)
    def response(self,data):
        try:
            match data:
                case dict():
                    response_input = ResponseInput(**data)
                    
                case list():
                    response_input = ResponseInput(
                        input=[{"role": item["role"], "content": item["content"]} for item in data],
                        model=default_config.model.value
                    )
            response = self.client.responses.create(
                **response_input.model_dump()
            )
            logging.info("API call successful")
            return response
        except Exception as e:
            logging.error(f"API call failed: {e}")
            return None

        
def debug():
    api_key = os.getenv("OPENROUTER_API_KEY")
    client = OpenRouterClient(api_key=api_key)
    return client



if __name__ == "__main__":
    
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  
    filemode='a'        
    )
    logging.debug(default_config.model.value)
    client = OpenRouterClient(api_key=os.getenv("OPENROUTER_API_KEY"))
    test_message = [
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
    logging.debug("Starting test message response")
    response = client.response(test_message)
    if response:
        print(response.output_text)
    logging.debug("Finished test message response")
    
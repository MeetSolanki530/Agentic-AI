from dotenv import load_dotenv
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

load_dotenv()

def get_model_client():

    model_client = OpenAIChatCompletionClient(api_key=os.getenv("GOOGLE_API_KEY"),model=MODEL,
                                              base_url="https://api.cerebras.ai/v1",
                                              model_capabilities={"function_calling" : True,"vision" : True,"json_output" : True})

    return model_client


from config.settings import OPEN_API_KEY, MODEL, MAX_TURN, MAX_TURN_10, TERMINATION_WORD
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
    model= MODEL,
    api_key = OPEN_API_KEY,
    base_url="http://localhost:11434/v1",
    model_capabilities={"function_calling" : True,"vision" : True,"json_output" : True}
    )


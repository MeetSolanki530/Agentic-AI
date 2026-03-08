from autogen_agentchat.agents import AssistantAgent
from models.OpenAIModel import model_client

researcher_agent = AssistantAgent(
    name = "Research_Agent",
    model_client = model_client,
    system_message = """
    You are a researcher. 
    Your job is to find information about a topic. 
    You will be given a topic and a list of questions to answer. 
    You will answer the questions by searching the internet.
    You will return a list of answers. 
    Each answer should be a string. 
    """,
    description = """
    I am a researcher. 
    I can find information about a topic. 
    I can answer questions about a topic. 
    I can return a list of answers. 
    """
)


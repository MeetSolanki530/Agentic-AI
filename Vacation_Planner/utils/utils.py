from autogen_agentchat.conditions import TextMentionTermination,MaxMessageTermination
from config.settings import TERMINATION_WORD,MAX_TURN, MAX_TURN_10
import json

text_termination = TextMentionTermination(TERMINATION_WORD) | MaxMessageTermination(MAX_TURN_10)

def save_state(agent,filename):
    """
    Saves the state of the agent to a file.
    """
    state = agent.save_state()
    with open(filename, 'w') as f:
        json.dump(state, f)

def load_state(agent,filename):
    """
    Loads the state of the agent from a file.
    """
    with open(filename, 'r') as f:
        state = json.load(f)
    agent.load_state(state)

def get_termination_condition():
    return text_termination
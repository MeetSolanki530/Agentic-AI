import pytest
from agents.planner import planner_agent

def test_planner_agent():
    """
    This function tests the planner agent.
    """
    assert planner_agent.name == "Travel_Planner"
    assert planner_agent.description == "A travel planner agent that helps users plan their trips."
    assert planner_agent.system_message == "You are a travel planner agent. Your task is to help users plan their trips by providing information about destinations,itineraries and travel tips."
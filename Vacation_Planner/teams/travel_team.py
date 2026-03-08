from autogen_agentchat.teams import RoundRobinGroupChat
from agents.planner import planner_agent
from agents.researcher import researcher_agent
from utils.utils import get_termination_condition


travel_plan_team = RoundRobinGroupChat(
    name="travel_plan_team",
    participants=[
     researcher_agent,
     planner_agent,
    ],
    termination_condition=get_termination_condition()
)
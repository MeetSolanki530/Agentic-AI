import os
from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "MeetSolanki/MeetAI:latest" #'gemini-2.5-flash'
MAX_TURN = 2
MAX_TURN_10 = 3
TERMINATION_WORD = 'stop'
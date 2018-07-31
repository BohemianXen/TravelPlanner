from enum import Enum

class StateMachine(Enum):
    WELCOME = 0
    LOGIN = 1
    HOME = 2
    SETTINGS = 3

    # def get_state(self)
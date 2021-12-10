from enum import Enum, auto

class OptionType(Enum):
    CALL = auto()
    PUT = auto()

# I can probably just save the dict from the resp
class OptionListing:
    def __init__(self, type, strike, expiration, resp_dict):
        pass



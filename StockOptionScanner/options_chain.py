import json

class OptionsChain:
    def __init__(self, chain_resp_json):
        self.calls = chain_resp_json['callExpDateMap']
        self.puts = chain_resp_json['putExpDateMap']

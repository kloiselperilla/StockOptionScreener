from multileg_trade import MultilegTrade

class VerticalSpread(MultilegTrade):
    """Can be any simple vertical spread, as long as these conditions are met:
        - Both legs are of the same type (call or put)
        - One leg is a long, and one is a write
    """
    def __init__(self, ticker, opt1, opt2):
        pass

    def validate(self):
        pass

    def check_against_criteria(self, criteria):
        pass

    def to_row(self):
        pass

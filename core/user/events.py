from core.common.events import Event
from decimal import Decimal

class DonateEvent(Event):
    def __init__(self, user_id: str, campaign_id: str, amount: Decimal) -> None:
        #TODO
        pass


class BuyEvent(Event):
    def __init__(self, user_id: str, product_id: str) -> None:
        #TODO
        pass
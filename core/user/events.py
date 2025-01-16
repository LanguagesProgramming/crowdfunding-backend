from core.common.events import Event
from decimal import Decimal

class DonateEvent(Event):
    def __init__(self, user_id: str, campaign_id: str, amount: Decimal) -> None:
        self.user_id = user_id
        self.campaign_id = campaign_id
        self.amount = amount


class BuyEvent(Event):
    def __init__(self, user_id: str, product_id: str) -> None:
        self.user_id = user_id
        self.product_id = product_id
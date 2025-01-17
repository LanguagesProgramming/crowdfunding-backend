from core.common.events import Event

class AddCampaignImageEvent(Event):
    def __init__(self, campaign_id: str, image: str) -> None:
        self.campaign_id = campaign_id
        self.image = image


class AddProductImageEvent(Event):
    def __init__(self, product_id: str, image: str) -> None:
        self.product_id = product_id
        self.image = image


class DeleteCampaignImageEvent(Event):
    def __init__(self, campaign_id: str, image: str) -> None:
        self.campaign_id = campaign_id
        self.image = image


class DeleteProductImageEvent(Event):
    def __init__(self, product_id: str, image: str) -> None:
        self.product_id = product_id
        self.image = image
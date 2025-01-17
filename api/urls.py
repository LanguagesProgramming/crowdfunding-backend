from .views import UserApi, CampaignApi, ProductApi, DonationApi, BuyApi, CampaignMediaApi, ProductMediaApi
from django.urls import path

urlpatterns = [
    path('user', UserApi.as_view()),
    path('user/<str:user_id>', UserApi.as_view()),
    path('campaign/<str:name>/<str:category>', CampaignApi.as_view()),
    path('campaign', CampaignApi.as_view()),
    path('campaign/<str:campaign_id>', CampaignApi.as_view()),
    path('campaign/media', CampaignMediaApi.as_view()),
    path('campaign/media/<str:campaign_id>/<str:image>', CampaignMediaApi.as_view()),
    path('product', ProductApi.as_view()),
    path('product/media', ProductMediaApi.as_view()),
    path('product/media/<str:product_id>/<str:image>', ProductMediaApi.as_view()),
    path('donate', DonationApi.as_view()),
    path('buy', BuyApi.as_view()),
]
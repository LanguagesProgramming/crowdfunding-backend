from .views import UserApi, CampaignApi, ProductApi, DonationApi, BuyApi, CampaignMediaApi, ProductMediaApi
from django.urls import path, re_path

urlpatterns = [
    path('user', UserApi.as_view()),
    re_path(r'^user/(?P<user_id>[^/]+)?/?$', UserApi.as_view()),
    re_path(r'^campaign/(?:(?P<name>[a-zA-Z0-9_]+)/)?(?:(?P<category>[a-zA-Z0-9_]+)/)?$', CampaignApi.as_view()),
    path('campaign', CampaignApi.as_view()),
    path('campaign/<str:campaign_id>', CampaignApi.as_view()),
    path('campaign/media', CampaignMediaApi.as_view()),
    path('campaign/media/<str:campaign_id>/<str:image>', CampaignMediaApi.as_view()),
    path('product', ProductApi.as_view()),
    path('product/media', ProductMediaApi.as_view()),
    path('product/media/<str:product_id>/<str:image>', ProductMediaApi.as_view()),
    path('donate', DonationApi.as_view()),
    path('buy', BuyApi.as_view()),
    path('buy/<str:user_id>', BuyApi.as_view()),
]
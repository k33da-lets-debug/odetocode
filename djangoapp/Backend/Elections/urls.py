from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_request, name='login'),
    path('campaigns', views.displayOnGoingCampaigns, name='campaign_list'),
    path('campaign_detail/<int:pk>/', views.displayCampaignDetails, name='campaign_detail'),
    path("logout", views.logout_request, name="logout"),
]



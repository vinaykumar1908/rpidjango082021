from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='BPCHome'),
    path('Enter_BPC/', views.Enter_BPC, name='Enter_BPC'),
    path('Show_BPC/', views.Show_BPC.as_view(), name='Show_BPC'),

]

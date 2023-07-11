from django.urls import path
from .views import slowDownAndWasteMemory, top_sellers

urlpatterns = [
    path('', slowDownAndWasteMemory, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    
]

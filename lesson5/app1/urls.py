from django.urls import path
from .views import slowDownAndWasteMemory, top_sellers

urlpatterns = [
    path('', slowDownAndWasteMemory, name='main'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    
]

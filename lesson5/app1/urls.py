from django.urls import path
from .views import main_page, top_sellers

urlpatterns = [
    path('', main_page, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
]

from django.shortcuts import render


def main_page(request):
    return render(request, 'index.html')


def top_sellers(request):
    return render(request, 'top-sellers.html')

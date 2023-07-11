from django.shortcuts import render


def top_sellers(request):
    return render(request, 'app1/top-sellers.html')


def fiba(num):
    if num in (1, 2):
        return 1
    return fiba(num-1) + fiba(num-2)


def slowDownAndWasteMemory(request):
    dick = {
        'num': fiba(10),
    }
    return render(request, 'app1/index.html')

if __name__ == '__main__':
    print(fiba(5))
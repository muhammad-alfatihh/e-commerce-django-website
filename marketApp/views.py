from django.shortcuts import render


def index(request):
    return render(request, 'marketApp/index.html')

def contact(request):
    return render(request, 'marketApp/contact.html')
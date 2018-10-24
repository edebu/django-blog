from django.shortcuts import render, HttpResponse
from .models import AddLink


def home_view(request):
    if request.user.is_authenticated():
        link = AddLink(request.POST or None)
        context = {
            'isim': 'Barış',
            'link': link,
        }
        

    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'home.html', context)


def about_view(request):

	return render(request, 'about.html')
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import AddLink


def home_view(request):
    if request.user.is_authenticated():
        link = get_object_or_404(AddLink)
        links = AddLink.objects.all()
        listlink = link.split('"')
        context = {
            'isim': 'Barış',
            'link': link,
            'links':links,

        }
        linkdic = {
            'src':listlink[1],
            'height':listlink[3],
            'widht':listlink[5],
            'frameborder':listlink[7],
            'allowfullscreen':listlink[9],
        }
        context['link'] = linkdic

    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'home.html', context )


def about_view(request):

	return render(request, 'about.html')
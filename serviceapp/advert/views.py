from django.shortcuts import render, HttpResponse


# Create your views here. #11.ders 13 14
def advert_detail(request):
    return render(request, 'advertdetail.html')


def advert_list(request):
    return render(request, 'listAdverts.html')


def advert_create(request):

    return render(request, 'advert.html', {'isim': 'asya'})

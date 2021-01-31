from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'main.html')


def home_view2(request):
    return render(request, 'main2.html')


def cat_view(request):
    return render(request, 'categories.html')
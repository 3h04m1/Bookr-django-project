from django.shortcuts import render


def index(request):
    return render(request,'react/index.html')


# Create your views here.

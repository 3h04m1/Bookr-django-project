from django.shortcuts import render


def index(request):
    names = "john,doe,mark,swain"
    return render(request, "index.html", {"names": names})


def greeting_view(request):
    username = request.user
    greet = 'Hai noroc'
    books = {'The night rider': 'Ben Author',
             'The justice': 'Don Abeman'}
    if str(request.user) == 'AnonymousUser':
        username = ""
    return render(request, ('simple-tag.html'), {"username": username, 'greet': greet, 'books': books})

# Create your views here.

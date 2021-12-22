from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



def greeting_view(request):

    return HttpResponse("Hey There, welcome to bookr! Your one stop place to review Books.")


@login_required
def greeting_view_user(request):
    user = request.user
    return HttpResponse(f"Hey There, welcome to bookr, <em>{user.username}</em>!")
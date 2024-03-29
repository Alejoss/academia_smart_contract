from http import HTTPStatus

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def profile(request):
    template = "profiles/profile.html"
    context = {}
    return render(request, template, context)


def create_profile(request):
    if request.is_ajax() and request.method == "POST":
        template = "profiles/create_profile_succesfull.html"
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        # TODO send email to confirm account
        return render(request, template, {"user": user})
    else:
        return HttpResponse(status=HTTPStatus.FORBIDDEN)


def complete_account(request):  # TODO implement % complete profile?
    pass

from django.shortcuts import render, HttpResponse, redirect
from dyn_gc_App.models import User


def cantLoginAfterLogin(get_response):
    def middleware(request):
        user = request.session.get("name")
        print(user)
        if user:
            print("ur already logged-in")
            return redirect('/')
        else:
            print("please Login")
            return get_response(request)

    return middleware
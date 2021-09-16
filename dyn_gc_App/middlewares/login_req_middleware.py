from django.shortcuts import render, HttpResponse, redirect
from os import path


def login_required(get_response):

    def middleware(request):

        print("Middleware...///")
        user = request.session.get("user")
        print(user)
        if user:
            response = None
            if user:
                response = get_response(request)
                # if user_id:
                #     state = get_response(request, user_id=user.id)
                #     print(state)
                # else:
                #     state = get_response(request)
            else:
                response = get_response(request)
            return response
            print(response)

        else:
            print("please Login")
            # url = request.path
            # print(url)
            #return redirect('/login/')
            return redirect('/login')

    return middleware
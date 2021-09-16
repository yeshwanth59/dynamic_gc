from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from .models import User, Master, Plot
from .forms import RegistrationForm, LoginForm
# Create your views here.


def home(request):
    img = Master.objects.all()
    return render(request, "home.html", {"img": img})


def plot(request):
    plot = Plot.objects.all()
    return render(request, "plots.html", {"plot": plot})


def srinfra(request):
    user = User.objects.all()
    return render(request, "SRinfra.html", {"user": user})


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration completed successfully")
    else:
        form = RegistrationForm()
        return render(request, "signup.html", {"form": form})


# def login(request):
#     if request.method == "POST":
#         my_loginform = LoginForm(request.POST)
#         if my_loginform.is_valid():
#             un = my_loginform.cleaned_data['username']
#             pwd = my_loginform.cleaned_data['password']
#             dbuser = User.objects.filter(username=un, password=pwd)
#
#             if not dbuser:
#                 return HttpResponse("Login Failed ")
#             else:
#                 return render(request, "SRinfra.html")
#
#     else:
#         my_form = LoginForm()
#         return render(request, "login.html", {"my_form": my_form})
#


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, "login.html")

    def post(self, request):
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un = MyLoginForm.cleaned_data["username"]
            pw = MyLoginForm.cleaned_data["password"]
            print(un)
            print(pw)
            user = User.objects.get(username=un, password=pw)
            dbuser = User.objects.filter(username=un, password=pw)

            temp = {}
            temp['name'] = user.username
            # temp['id'] = user.id
            # temp['mobileNo'] = user.mobileNo
            # temp['email'] = user.email
            # temp['pwd'] = user.pwd
            request.session['user'] = temp
            print(user.__dict__)
            if Login:
                return redirect("/home")
            else:
                return redirect("/signup")

            if not dbuser.username:
                return HttpResponse("Login Failed")

            else:
                return redirect("/signup")
        else:
            my_form = LoginForm()
        return render(request, "login.html", {"my_form": my_form})


def contact(request):
    return render(request, "contact_us.html")


def logout(request):
    request.session.clear()
    return redirect("/")


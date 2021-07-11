from django.shortcuts import render, redirect
from .forms import signUpForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# this is login form


def home(request):
    form = LoginForm()
    if(request.method == "POST"):
        try:
            form = LoginForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                print("This is valid")
                user = form.get_user()
                login(request, user)
                return redirect('homePage')
            else:
                print("this is not valid")

        except Exception as e:
            print(e)
            raise

    stuff_for_frontend = {
        'form': form,
    }
    return render(request, 'accounts/home.html', stuff_for_frontend)


# this is sign up form

def sign_up(request):
    form = signUpForm()
    if request.method == "POST":
        try:
            form = signUpForm(request.POST)
            if form.is_valid():
                # here we make the user
                user = form.save()
                login(request, user)
                return redirect('homePage')
        except Exception as e:
            print(e)
            raise

    stuff_for_frontend = {
        'form': form,
    }
    return render(request, 'accounts/sign_up.html', stuff_for_frontend)


@login_required(login_url='home')
def logoutPage(request):
    logout(request)
    return redirect('home')


# if we do not use the form functionality of Django, we have to do following and we have to make the models
# def createNewAccount(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         models.NewUserLogin.objects.create(name=email,password=password)

#     return render(request,'accounts/sign_up.html')

# def loginUser(request):
#     if request.method == "POST":
#         try:
#             form = LoginForm(data=request.POST)
#             print(form.errors)
#             if form.is_valid():
#                 print("form is valid")
#                 user = form.get_user()
#                 login(request,user)
#                 return redirect('homePage')
#             else:
#                 print("form is not valid")
#         except Exception as e:
#             print(e)
#             raise

    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     try:
    #         models.NewUserLogin.objects.get(name=email,password=password)

    #         print("User and Possword is correct")
    #     except:
    #         try:
    #             models.NewUserLogin.objects.get(name=email)
    #             print("possword is incorrenct")
    #             render(request,'accounts/home.html')
    #         except:
    #             print("Plese sign up there is no account like this ")
    #             return render(request,'accounts/sign_up.html')

    # return render(request,'blog/blogHome.html')

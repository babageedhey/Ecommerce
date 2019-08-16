from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout as django_logout

# Create your views here.

def signup(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Validate Password Match
        if password == password2:
            #Validate unique username
            if User.objects.filter(username=username).exists():
                #Username already exists
                return redirect('signup')
            else:
                #Email already exists
                if User.objects.filter(email=email).exists():
                    #Email already exists
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            return redirect ('signup')

    return render(request, 'accounts/register.html')


def login(request):
   
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        context = {
            'username': username
        }
        #Check that User is not empty
        if user is not None:
            auth.login(request, user)
            return render (request ,'accounts/dashboard.html', context)
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')


def dashboard(request):
    context = {
        'username': username
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    print('logged out')
    django_logout(request)

    return  redirect('index')
    
from django.shortcuts import render
from .models import Contact 
# Create your views here.

#Home Page View
def index(request):
    context = {

    }
    return render(request, 'home/home.html', context)

#About Us View
def about(request):
    context = {

    }
    return render(request,'home/about.html', context)

#COntact Us View
def contact(request):
    context = {
        
    }
    if request.method == "POST":
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'home/contact.html', context)

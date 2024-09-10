from django.shortcuts import render

def about(request):
    context={}
    return render(request, "myApp/about.html", context)

def contact(request):
    context={}
    return render(request, "myApp/contact.html", context)

def homemenu(request):
    context={}
    return render(request, "myApp/homemenu.html", context)

def home(request):
    context={}
    return render(request, "myApp/home.html", context)

def services(request):
    context={}
    return render(request, "myApp/services.html", context)



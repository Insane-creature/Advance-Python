from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'I am value.'
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is Homepage.")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is About page.")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is Services page.")

def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("This is Contact page.")

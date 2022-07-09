from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'gym.html')
def about(request):
    return HttpResponse("about page")
def contact(request):
    return HttpResponse("contact page")
def service(request):
    return HttpResponse("service page")


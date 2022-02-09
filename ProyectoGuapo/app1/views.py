from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == "POST":
        data = request.POST.get("textfield", None)
        html = ("<H1>%s</H1>", data)
        return HttpResponse(html)

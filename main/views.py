from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@csrf_protect
@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')

@csrf_protect
@ensure_csrf_cookie
def about(request):
    return render(request, 'about.html')

@csrf_protect
@ensure_csrf_cookie
def warranty_service(request):
    return render(request, 'warranty.html')

@csrf_protect
@ensure_csrf_cookie
def service_area(request):
    return render(request, 'service_area.html')

@csrf_protect
@ensure_csrf_cookie
def contact(request):
    return render(request, 'contact.html')

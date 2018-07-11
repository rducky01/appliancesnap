from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@csrf_protect
@ensure_csrf_cookie
def index(request):
    return render_to_response('index.html')

@csrf_protect
@ensure_csrf_cookie
def about(request):
    return render_to_response('about.html')

@csrf_protect
@ensure_csrf_cookie
def service_area(request):
    return render_to_response('service_area.html')

@csrf_protect
@ensure_csrf_cookie
def contact(request):
    return render_to_response('contact.html')

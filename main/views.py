from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@csrf_protect
@ensure_csrf_cookie
def index(request):
    return render_to_response('index.html')

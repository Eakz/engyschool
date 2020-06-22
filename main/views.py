import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def index(request):
    path = settings.MEDIA_ROOT
    context = {'images' : path}
    return render(request, "main/index.html",context)
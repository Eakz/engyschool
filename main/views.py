import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
# from .models import Faq

# Create your views here.


def index(request):
    faqs = Faq.objects.all()[0:6]
    faqs_up = faqs[0:3]
    faqs_down = faqs[3:6]
    path = settings.MEDIA_ROOT
    context = {'images': path, 'faqs_up': faqs_up, 'faqs_down': faqs_down}
    return render(request, "main/index.html", context)

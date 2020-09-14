import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from .models import Faq

# Create your views here.


def index(request):
    faqs = Faq.objects.all()[0:6]
    faqsup = faqs[0:3]
    faqsdown = faqs[3:6]
    path = settings.MEDIA_ROOT
    context = {'images': path, 'faqsup': faqsup, 'faqsdown': faqsdown}
    return render(request, "main/index.html", context)

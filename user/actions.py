import os

from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string



def generate_pdf(request):
    context = {
        "recruit": request.user
    }
    response = render_to_string('template.html', context=context)

    return HttpResponse(response)

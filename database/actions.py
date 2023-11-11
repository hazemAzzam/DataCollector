import os

from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string



@admin.action(description="Generate Report")
def generate_pdf(modeladmin, request, queryset):
    for obj in queryset:   
        context = {
            "recruit": obj
        }
        response = render_to_string('template.html', context=context)

        return HttpResponse(response)

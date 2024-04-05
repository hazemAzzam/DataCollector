from django.contrib import admin
from django.http import HttpRequest

from .models import *
from .actions import generate_pdf

@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'triple_digit',
        'mobile_number',
    )
    fieldsets=(
        ('Personal Information', {
            'fields': (
                ('name', 'education'),
                ('date_of_birth', 'birth_location'),
                ('marital_status', 'number_of_children'),
                ('residence', 'triple_digit'),
                ('mobile_number')
            )
        }),
    )
    actions=[generate_pdf]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
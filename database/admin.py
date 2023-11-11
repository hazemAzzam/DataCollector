from django.contrib import admin

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

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'relate',
        'recruit',
    )
    fieldsets=(
        ('', {
            'fields': (
                'recruit',
                'relate',
                'name',
                'religion',
                'nationality',
                'job',
                'date_of_birth',
                'birth_location',
                'residence',
            ),
        }),
    )
    

@admin.register(Brother)
class BrotherAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'recruit',
    )
    fieldsets=(
        ('', {
            'fields': (
                'recruit',
                'name',
                'date_of_birth',
                'job',
                'wife_name',
                'wife_job',
                'residence',
            ),
        }),
    )

@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'wife_name',
        'relate',
        'date_of_birth',
        'recruit',
    )
    fieldsets=(
        ('', {
            'fields': (
                'recruit',
                'relate',
                'name',
                'date_of_birth',
                'job',
                'wife_name',
                'wife_job',
                'residence'
            )
        }),
    )
    list_filter=(
        'relate',
    )
    search_fields=(
        'name',
        'wife_name',
    )
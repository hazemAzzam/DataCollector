from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import *

class DefaultAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.recruit = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request: HttpRequest):
        queryset = self.model.objects.filter(recruit=request.user)
        return queryset
    
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return True
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return True
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return True
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return True
    
    def has_module_permission(self, request: HttpRequest) -> bool:
        return True

@admin.register(Parent)
class ParentAdmin(DefaultAdmin):
    list_display=(
        'name',
        'relate',
    )
    fieldsets=(
        ('', {
            'fields': (
                'relate',
                'name',
                'nationality',
                'qualification',
                'job',
                'military_officer',
                'residence',
            ),
        }),
    )
    

@admin.register(Supports)
class SupportsAdmin(DefaultAdmin):
    list_display=(
        'name',
        'relate',
    )
    fieldsets=(
        ('', {
            'fields': (
                'name',
                'relate',
                'nationality',
                'date_of_birth',
                'national_number',
                'notes',
            )
        }),
    )

@admin.register(Brother)
class BrotherAdmin(DefaultAdmin):
    list_display=(
        'name',
    )
    fieldsets=(
        ('', {
            'fields': (
                'name',
                'relate',
                'qualification',
                'job',
                'military_officer',
                'spouse_name',
                'spouse_qualification',
                'spouse_job',
                'residence',
            ),
        }),
    )    
    
@admin.register(Relative)
class RelativeAdmin(DefaultAdmin):
    list_display=(
        'name',
        'spouse_name',
        'relate',
    )
    fieldsets=(
        ('', {
            'fields': (
                'relate',
                'name',
                'qualification',
                'job',
                'spouse_name',
                'spouse_job',
                'residence'
            )
        }),
    )
    list_filter=(
        'relate',
    )
    search_fields=(
        'name',
        'spouse_name',
    )

@admin.register(Current_Wife_Data)
class Current_Wife_Data_Admin(DefaultAdmin):
    fieldsets=(
        ('', {
            'fields': (
                'statement',
                'name',
                'nationality',
                'religion',
                'qualification',
                'job',
                'residence'
            )
        }),
    )

@admin.register(Wife_Borther)
class Wife_Borther_Admin(DefaultAdmin):
    fieldsets=(
        ('', {
            'fields': (
                'name',
                'gender',
                'qualification',
                'job',
                'spouse_name',
                'spouse_job',
                'residence'
            )
        }),
    )
    
    
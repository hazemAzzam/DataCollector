from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import *

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'relate',
    )
    fieldsets=(
        ('', {
            'fields': (
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
    
    def save_model(self, request, obj, form, change):
        obj.recruit = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request: HttpRequest):
        queryset = self.model.objects.filter(recruit=request.user)
        return queryset
    
    #def has_add_permission(self, request: HttpRequest) -> bool:
    #    return True
    #
    #def has_view_permission(self, request: HttpRequest) -> bool:
    #    return True
    #
    #def has_delete_permission(self, request: HttpRequest) -> bool:
    #    return True
    #
    #def has_change_permission(self, request: HttpRequest) -> bool:
    #    return True
    
    def has_module_permission(self, request: HttpRequest) -> bool:
        return True


@admin.register(Brother)
class BrotherAdmin(admin.ModelAdmin):
    list_display=(
        'name',
    )
    fieldsets=(
        ('', {
            'fields': (
                'name',
                'date_of_birth',
                'job',
                'wife_name',
                'wife_job',
                'residence',
            ),
        }),
    )
    def save_model(self, request, obj, form, change):
        obj.recruit = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request: HttpRequest):
        queryset = self.model.objects.filter(recruit=request.user)
        return queryset

@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'wife_name',
        'relate',
        'date_of_birth',
    )
    fieldsets=(
        ('', {
            'fields': (
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
    def save_model(self, request, obj, form, change):
        obj.recruit = request.user
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request: HttpRequest):
        queryset = self.model.objects.filter(recruit=request.user)
        return queryset
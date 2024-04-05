from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
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
        ('Account Information', {
            'fields': (
                'code',
                'password',
                'is_staff',
                'user_permissions',
            )
        }),
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

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        if (request.user.is_superuser):
            return super().get_queryset(request)
        else:
            return Recruit.objects.filter(code=request.user.code)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_superuser
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        data = request.POST.copy() 

        password = data.pop('password', None)

        if not change:
            obj.set_password(password[0])

        super().save_model(request, obj, form, change)

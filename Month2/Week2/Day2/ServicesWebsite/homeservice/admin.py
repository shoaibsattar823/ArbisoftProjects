# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Service, Customer, Order
# Register your models here.


class OrderInline(admin.TabularInline):
    model = Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    inlines = (OrderInline, )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def username(obj):
        return obj.ordered_by.username
    # username = Order.ordered_by.username
    list_display = ('ordered_service', 'ordered_by',
                    username, 'ordered_date', 'status')
    list_filter = ('ordered_by', 'ordered_by__first_name')
    list_display_links = ('ordered_service',)
    list_editable = ('status',)
    # list_select_related = ('ordered_service', 'ordered_by')
    search_fields = ['ordered_by__username']
    fieldsets = (
        (None, {
            'fields': ('ordered_service',
                       'ordered_by', 'ordered_date', 'status')
        }),
        ('Advanced Options', {
            # 'classes': ('collapse',),
            'fields': ('urgency',)
        })
    )


class ServiceAdmin(admin.ModelAdmin):
    inlines = [OrderInline, ]

# def change_view(self, request, object_id, form_url='', extra_context=None):


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
# admin.site.register(Customer)
# admin.site.register(Order)

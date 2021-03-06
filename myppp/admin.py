# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from myppp.models import Fringe_type, Accessory_type, Fabric_type, Fabric_subtype, Size_type, Colors, Painters, My_ppp
from django.conf import settings

class Fringe_typeAdmin(admin.ModelAdmin):
    list_display = ('fringe_type',)
    search_fields = ("fringe_type",)
    list_filter = ("fringe_type",) 

admin.site.register(Fringe_type, Fringe_typeAdmin)

class PaintersAdmin(admin.ModelAdmin):
    list_display = ('painter',)
    search_fields = ("painter",)
    list_filter = ("painter",) 

admin.site.register(Painters, PaintersAdmin)

class Accessory_typeAdmin(admin.ModelAdmin):
    list_display = ('accessory_type',)
    search_fields = ("accessory_type",)
    list_filter = ("accessory_type",) 

admin.site.register(Accessory_type, Accessory_typeAdmin)

class Fabric_typeAdmin(admin.ModelAdmin):
    list_display = ('fabric_type',)
    search_fields = ("fabric_type",)
    list_filter = ("fabric_type",) 

admin.site.register(Fabric_type, Fabric_typeAdmin)


class Fabric_subtypeAdmin(admin.ModelAdmin):
    list_display = ('fabric_type','fabric_subtype',)
    search_fields = ("fabric_type","fabric_subtype",)
    list_filter = ("fabric_type","fabric_subtype",) 

admin.site.register(Fabric_subtype, Fabric_subtypeAdmin)

class Size_typeAdmin(admin.ModelAdmin):
    list_display = ('size_type',)
    search_fields = ("size_type",)
    list_filter = ("size_type",) 

admin.site.register(Size_type, Size_typeAdmin)

class ColorsAdmin(admin.ModelAdmin):
    list_display = ('color', 'color_pic')
    search_fields = ('color', 'color_pic')
    list_filter = ('color', 'color_pic') 

admin.site.register(Colors, ColorsAdmin)

class My_pppAdmin(admin.ModelAdmin):
    list_display = ('name', 'painter', 'accessory_type', 'fabric_type', 'fabric_subtype', 'size_type', 'fringe_type', 'border_color', 'base_color', 'color1', 'color2', 'color3', 'image')
    search_fields = ('name', 'painter', 'accessory_type', 'fabric_type', 'fabric_subtype', 'size_type', 'fringe_type', 'border_color', 'base_color')
    list_filter = ('name', 'painter', 'accessory_type', 'fabric_type', 'fabric_subtype', 'size_type', 'fringe_type', 'border_color', 'base_color') 

admin.site.register(My_ppp, My_pppAdmin)

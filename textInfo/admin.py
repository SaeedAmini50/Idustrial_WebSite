from django.contrib import admin
from .models import TextEntry, Category, Number, HeaderInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(TextEntry)
class TextEntryAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'entry_id', 'title', 'category', 'is_visible', 'select_option', 'created_at')
    list_filter = ('category', 'is_visible', 'select_option', 'created_at')
    search_fields = ('unique_id', 'entry_id', 'title', 'content')
    readonly_fields = ('entry_id', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'select_option')
    ordering = ('unique_id',)
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('unique_id', 'title', 'content', 'category', 'image')
        }),
        ('تنظیمات نمایش', {
            'fields': ('is_visible', 'select_option')
        }),
        ('اطلاعات سیستمی', {
            'fields': ('entry_id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )



@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')    
    search_fields = ('name',)
    
@admin.register(HeaderInfo)
class HeaderInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone', 'working_hours')
    search_fields = ('company_name', 'email', 'phone')
    fields = ('company_name', 'email', 'phone', 'working_hours', 'logo')

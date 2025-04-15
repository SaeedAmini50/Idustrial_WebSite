from django.contrib import admin
from .models import TextEntry, Category, Number, HeaderInfo, FooterInfo, CompanyInfo, Service, Employee


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(TextEntry)
class TextEntryAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'entry_id', 'title', 'category', 'is_visible', 'title_size', 'created_at')
    list_filter = ('category', 'is_visible', 'title_size', 'created_at')
    search_fields = ('unique_id', 'entry_id', 'title', 'content')
    readonly_fields = ('entry_id', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'title_size')
    ordering = ('unique_id',)
 

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('unique_id', 'title', 'content', 'category', 'image')
        }),
        ('تنظیمات نمایش', {
            'fields': ('is_visible', 'title_size', 'display_order')
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

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location')
    search_fields = ('email', 'phone', 'location')
    fields = ('email', 'phone', 'location', 'telegram_link', 'aparat_link', 'whatsapp_link', 'facebook_link', 'instagram_link')

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'image')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible', 'service_link')
    list_filter = ('is_visible',)
    search_fields = ('title', 'content', 'service_link')
    fields = ('title', 'content', 'image', 'service_link', 'is_visible')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'email', 'phone', 'is_visible')
    list_filter = ('is_visible', 'job_title')
    search_fields = ('first_name', 'last_name', 'job_title', 'email', 'phone')
    fields = ('first_name', 'last_name', 'job_title', 'email', 'phone', 'whatsapp_link', 'telegram_link', 'image', 'is_visible')

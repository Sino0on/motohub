from django.contrib import admin
from .models import *


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('current_text', 'original_text')  # Display these fields in the list view
    readonly_fields = ('original_text',)  # Prevent modification of the original text
    search_fields = ('original_text', 'current_text')  # Allow searching by both original and current text

    fieldsets = (
        (None, {
            'fields': ('original_text', 'current_text', 'current_text_ru', 'current_text_ky'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('original_text',)
        return self.readonly_fields


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_filter = ('title',)



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'created_at')
    search_fields = ('first_name', 'created_at')
    list_filter = ('first_name',)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')
    search_fields = ('name', 'profession')
    list_filter = ('profession',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'location', 'type')
    search_fields = ('title', 'client', 'location', 'type')
    list_filter = ('client', 'location', 'type')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'phone_number')
    search_fields = ('name', 'profession', 'phone_number')
    list_filter = ('profession',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


admin.site.register(SiteSetting)

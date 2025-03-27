from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'secondary_description')


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'profession')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'secondary_description')


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('profession', )


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(SiteContent)
class SiteContentTranslationOptions(TranslationOptions):
    fields = ('current_text', )

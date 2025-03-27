from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .filters import NewsFilter
from .forms import ApplicationForm
from .models import *


class HomePage(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['services'] = Service.objects.all()
        context['categories'] = Category.objects.all()
        context['employers'] = Employee.objects.all()
        context['advantages'] = Advantage.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['projects'] = Project.objects.all()
        context['news'] = News.objects.all()[:3]
        context['site'] = SiteSetting.objects.all().first()
        return context


class NewsListView(generic.ListView):
    queryset = News.objects.all()
    model = News
    template_name = 'news.html'
    paginate_by = 5
    context_object_name = 'news'
    filter_class = NewsFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = self.filter_class(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class NewsDetailView(generic.DetailView):
    queryset = News.objects.all()
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class ServiceDetailView(generic.DetailView):
    template_name = 'services-details.html'
    queryset = Service.objects.all()
    model = Service
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class ServiceListView(generic.ListView):
    template_name = 'services.html'
    queryset = Service.objects.all()
    model = Service
    context_object_name = 'services'

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['form'] = ApplicationForm
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class AboutUsView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['services'] = Service.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['employers'] = Employee.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class ProjectListView(generic.ListView):
    template_name = 'projects.html'
    queryset = Project.objects.all()
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class ProjectDetailView(generic.DetailView):
    template_name = 'project_detail.html'
    queryset = Project.objects.all()
    model = Project
    context_object_name = 'project'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['project'])
        context['about'] = SiteSetting.objects.all().first()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


class ContactUs(generic.FormView):
    form_class = ApplicationForm
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            if request.GET.get('product'):
                application = form.save(commit=False)
            application.save()
        return redirect('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm
        context['about'] = SiteSetting.objects.all().first()
        context['services'] = Service.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['new_news'] = News.objects.all()[:3]
        return context


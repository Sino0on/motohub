from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('about-us/', AboutUsView.as_view(), name='about'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

]

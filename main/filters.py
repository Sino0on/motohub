import django_filters
from .models import News
from django.db.models import Q
from django.shortcuts import get_object_or_404


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', method='filter_title')

    def filter_title(self, queryset, name, value):
        # print(len(queryset))
        search_term = value
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
        print('title')
        return queryset

    class Meta:
        model = News
        fields = ['title']
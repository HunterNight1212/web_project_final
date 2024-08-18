import django_filters
from django import forms
from django.forms import DateInput

from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from .models import Post, Author



class PostFilter(FilterSet):
    time_in = DateFilter(field_name='time_in', lookup_expr='date__gte', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'hat': ['icontains'],
            'author': ['exact'],
        }
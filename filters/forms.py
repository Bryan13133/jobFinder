from django import forms
from .models import Filters
from django.utils.translation import gettext_lazy as _
class FiltersForm(forms.ModelForm):
    # jobDescription = forms.CharField(label=_('Job Description'),widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    # country = forms.EmailField(label = ('Country'),widget=(forms.Select(attrs={'class': 'select-css'})),required=True)
    # jobType = forms.CharField(label=_('Job Type'),widget=(forms.Select(attrs={'class': 'select-css'})),required=True)
    # category = forms.CharField(label=_('Category'), widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    # skills = forms.CharField(label=_('Skills'), widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    # budget = forms.CharField(label=_('Budget'), widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    # daysPosted = forms.CharField(label=_('Days Posted'), widget=forms.Select(attrs={'class': 'select-css'}),required=True)
    # technology = forms.CharField(label=_('Technology'), widget=forms.Select(attrs={'class': 'select-css'}),required=True)
    
    
    
    
    class Meta:
        model = Filters
        fields = [
            'jobDescription',
            'country',        
            'jobType',        
            'skills',        
            'daysPosted',     
            'technology'   
        ]
        labels = {
            'jobDescription': 'Job Description',
            'country': 'Country',        
            'jobType': 'Job Type',       
            'skills': 'Skills',       
            'daysPosted': 'Days Posted',    
            'technology':  'Technology'
        }
        widgets = {
            'jobDescription': forms.TextInput(attrs={'class': 'text'}),
            'country':        forms.Select(attrs={'class': 'select-css'}),
            'jobType':        forms.Select(attrs={'class': 'select-css'}),
            'category':       forms.TextInput(attrs={'class': 'text'}),
            'skills':         forms.TextInput(attrs={'class': 'text'}),
            'daysPosted':     forms.Select(attrs={'class': 'select-css'}),
            'technology':     forms.Select(attrs={'class': 'select-css'}),
        }
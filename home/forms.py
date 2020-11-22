from django import forms
from .models import Filters

class FiltersForm(forms.ModelForm):
    
    class Meta:
        model = Filters
        fields = [
            'jobDescription',
            'country',        
            'jobType',        
            'category',      
            'skills',        
            'budget',        
            'daysPosted',     
            'technology'   
        ]
        widgets = {
            'jobDescription': forms.TextInput(attrs={'class': 'form-control'}),
            'country':        forms.Select(attrs={'class': 'select-css'}),
            'jobType':        forms.Select(attrs={'class': 'select-css'}),
            'category':       forms.TextInput(attrs={'class': 'form-control'}),
            'skills':         forms.TextInput(attrs={'class': 'form-control'}),
            'budget':         forms.TextInput(attrs={'class': 'form-control'}),
            'daysPosted':     forms.Select(attrs={'class': 'select-css'}),
            'technology':     forms.Select(attrs={'class': 'select-css'}),
        }

class FiltersForm2(forms.Form):
    jobDescription = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    country = forms.CharField(required=True,widget=forms.Select(attrs={"class":"select-css"}))        
    jobType = forms.CharField(required=True,widget=forms.Select(attrs={"class":"select-css"}))        
    category = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))      
    skills = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))        
    budget = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))      
    daysPosted = forms.CharField(required=True,widget=forms.Select(attrs={"class":"select-css"}))     
    technology = forms.CharField(required=True,widget=forms.Select(attrs={"class":"select-css"}))  

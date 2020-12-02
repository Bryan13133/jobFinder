from django.shortcuts import render
from .forms import FiltersForm2,FiltersForm
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
import requests
# Create your views here.
def home(request):
    logout(request)
    if request.method == 'POST':
        form = FiltersForm(request.POST)
        if form.is_valid():
            gitData = {
                'jobDescription': form.cleaned_data.get('jobDescription'),
                'country':        form.cleaned_data.get('country'),        
                'jobType':        form.cleaned_data.get('jobType'),                
            }
           
            response = requestGit(data=gitData)
            if(response):
                data = response.json()
                return render(request,'joblist.html',{'data':data})
            else:
                form = FiltersForm()
                context = {
                    'form': form
                }
                return render(request,'home.html')
    else:
        form = FiltersForm()
        context = {
            'form': form
        }
        return render(request,'home.html',context)

def requestGit(data):
    fullTime = True
    if data['jobType'] != 'FT':
        fullTime = False
    parameters = {
        "description": data['jobDescription'],
        "full_time": fullTime,
        "location": data['country']
    }
    response = requests.get("https://jobs.github.com/positions.json",params=parameters)
    return response 


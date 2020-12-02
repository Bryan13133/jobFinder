from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.core.cache import cache
from django.contrib.auth import logout

from .forms import FiltersForm
import requests
@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url="login/")
def filters(request):
    if request.user.is_authenticated:
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
                    return render(request,'jobs.html',{'data':data})
                else:
                    form = FiltersForm()
                    context = {
                        'form': form
                    }
                    return render(request,'filters.html')
        else:
            form = FiltersForm()
            context = {
                'form': form
            }
            return render(request,'filters.html',context)
    else:
        return redirect('404')

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
    
@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url="login/")
def logoutApp(request):
    logout(request)
    cache.clear()
    return redirect('home1')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url="login/")
def jobs(request):
    return render(request,'jobs.html')



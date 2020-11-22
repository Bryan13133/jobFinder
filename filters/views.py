from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import FiltersForm
import requests
@login_required(login_url="login/")
def filters(request):
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
                return render(request,'filters.html')
    else:
        form = FiltersForm()
        context = {
            'form': form
        }
        return render(request,'filters.html',context)

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

def logoutApp(request):
    logout(request)
    return redirect('home1')



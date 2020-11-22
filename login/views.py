from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
# Create your views here.
def loginApp(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=raw_password)
            form = LoginForm()
            if user is not None:
                login(request, user)
                return redirect('filters')
    else:
        form = LoginForm()
    return render(request,'login.html', {'form':form})
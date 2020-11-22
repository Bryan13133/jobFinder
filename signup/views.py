from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=raw_password)
            form = SignupForm()
            if user is not None:
                login(request, user)
                return redirect('filters')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
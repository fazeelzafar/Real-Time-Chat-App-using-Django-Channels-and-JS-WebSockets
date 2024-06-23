from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import signUpForm

# Create your views here.
def frontPage(request):
    return render(request, "core/base.html")

def signUp(request):
    form = signUpForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("frontPage")
    
    return render(request, "core/signup.html", {"form": form})

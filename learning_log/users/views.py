from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticate_user=authenticate(username=new_user.username,password=request.POST['password'])
            login(request,authenticate_user)
            return  HttpResponseRedirect(reverse('learning_logs:index'))


    content={'form':form}
    return render(request,'users/register.html',content)


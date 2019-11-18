from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'register.html',{'form':form})
    else:
        form=UserCreationForm()        
        return render(request,'register.html',{'form':form})


def login_me(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
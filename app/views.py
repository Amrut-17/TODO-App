from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as UserLogin, logout as UserLogout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import TODOForm
from .models import TODO


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        tasks = TODO.objects.filter(user = user).order_by('-priority')
        return render(request, 'app/home.html', {'form':form, 'tasks':tasks})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
    else:        
        form = UserCreationForm()
    return render(request, 'app/signup.html',{'form':form})

    # if request.method == 'GET':
    #     form = UserCreationForm()
    #     return render(request, 'app/signup.html', {'form':form})
    # else:
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         if user is not None:
    #             return redirect('home')
    #     else:
    #         return render(request, 'app/signup.html', {'form':form})




def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                UserLogin(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form':form})




def add_task(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            print(user)
            todo.save()
            return redirect('home')
        else:
            return render(request, 'app/home.html', {'form':form})





def logout(request):
    UserLogout(request)
    return redirect('login')


def delete_task(request, id):
    task = TODO.objects.get(pk=id).delete()
    return redirect('/')
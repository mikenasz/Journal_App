from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CreateEntryForm
from .models import journal



def index(request):
    entries = journal.objects.all()
    context = {'entries': entries}
    return render(request, 'entry/index.html', context)
def add(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateEntryForm()
    context = {'form': form}
    return render(request, 'entry/add.html',context)
def delete(request,id):

    entries = journal.objects.get(id=id)
    entries.delete()
    return redirect('index')





def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'User Authentication/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, 'User Authentication/login.html', context)
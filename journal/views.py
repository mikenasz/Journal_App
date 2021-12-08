from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CreateUserForm, CreateEntryForm, MoodForm, ActivitiesForm
from .models import journal, Mood, Activities


@login_required(login_url='login')
def index(request):
    entries = journal.objects.all()
    context = {'entries': entries}
    return render(request, 'entry/index.html', context)


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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'User Authentication/login.html', {'form': form})


def add(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateEntryForm()
    context = {'form': form}
    return render(request, 'entry/add.html', context)


def delete(request, id):
    entries = journal.objects.get(id=id)
    entries.delete()
    return redirect('index')


def moodPage(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')
    else:
        form = MoodForm()
    context = {'form': form}

    return render(request, 'entry/moods.html', context)


def activitiesPage(request):
    if request.method == 'POST':
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')
    else:
        form = ActivitiesForm()
    context = {'form': form}

    return render(request, 'entry/activities.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def chart(request):
    moods=Mood.objects.all()
    context={'moods':moods}
    return render(request, 'entry/chart.html',context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from online_library_django_template_project.profile_app.forms import CreateUserForm


@login_required
def home_page(request):
    user_profile = request.user.userprofile
    context = {
        'profile': user_profile,
    }
    return render(request=request, template_name='home-page.html', context=context)


def register_page(request):
    form = CreateUserForm
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login-page')

    return render(request=request, template_name='register-page.html', context=context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
    else:
        form = AuthenticationForm()

    return render(request, 'login-page.html', {'form': form})

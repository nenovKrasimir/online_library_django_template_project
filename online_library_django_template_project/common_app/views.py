from django.shortcuts import render, redirect
from online_library_django_template_project.profile_app.forms import CreateUserForm


def home_page(request):
    form = CreateUserForm
    context = {'profile': '', 'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    return render(request=request, template_name='home-page.html', context=context)

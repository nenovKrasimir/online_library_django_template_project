from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from online_library_django_template_project.profile_app.forms import CreateProfileForm
from online_library_django_template_project.profile_app.models import UserProfile


def home_page(request):
    profile = UserProfile.objects.first()
    form = UserCreationForm
    context = {'profile': profile, 'form': form}

    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    if profile:
        books = profile.books.all()
        context['books'] = books

    return render(request=request, template_name='home-page.html', context=context)

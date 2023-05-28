from django.shortcuts import render

from online_library_django_template_project.profile_app.forms import CreateProfileForm
from online_library_django_template_project.profile_app.models import UserProfile


def home_page(request):
    profile = UserProfile.objects.first()
    books = ""
    if profile:
        books = profile.books.all()

    form = CreateProfileForm(request.POST or None)
    context = {'profile': profile, 'form': form, 'books': books}
    return render(request=request, template_name='home-page.html', context=context)
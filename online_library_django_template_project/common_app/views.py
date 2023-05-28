from django.shortcuts import render

from online_library_django_template_project.profile_app.forms import CreateProfileForm
from online_library_django_template_project.profile_app.models import UserProfile


def home_page(request):
    profile = UserProfile.objects.first()
    form = CreateProfileForm(request.POST or None)
    context = {'profile': profile, 'form': form}
    return render(request=request, template_name='home-no-profile.html', context=context)
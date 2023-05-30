from django.shortcuts import render, redirect

from online_library_django_template_project.profile_app.forms import CreateUserForm
from online_library_django_template_project.profile_app.models import UserProfile


# Create your views here.
from django.shortcuts import render, redirect
from django.views import View

from online_library_django_template_project.profile_app.forms import CreateUserForm
from online_library_django_template_project.profile_app.models import UserProfile


class ProfileDetailView(View):
    def get(self, request):
        profile = UserProfile.objects.first()
        context = {'profile': profile}
        return render(request=request, template_name='profile.html', context=context)


class ProfileEditView(View):
    def get(self, request):
        profile = UserProfile.objects.first()
        form = CreateUserForm(instance=profile)
        context = {'profile': profile, 'form': form}
        return render(request=request, template_name='edit-profile.html', context=context)

    def post(self, request):
        profile = UserProfile.objects.first()
        form = CreateUserForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details-profile')

        context = {'profile': profile, 'form': form}
        return render(request=request, template_name='edit-profile.html', context=context)


class ProfileDeleteView(View):
    def get(self, request):
        profile = UserProfile.objects.first()
        form = CreateUserForm(instance=profile)

        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

        context = {'profile': profile, 'form': form}
        return render(request=request, template_name='delete-profile.html', context=context)

    def post(self, request):
        profile = UserProfile.objects.first()
        profile.delete()
        return redirect('home-page')

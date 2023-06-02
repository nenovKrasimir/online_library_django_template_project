from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from online_library_django_template_project.profile_app.forms import CreateUserForm, EditUserForm
from online_library_django_template_project.profile_app.models import UserProfile

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View

from online_library_django_template_project.profile_app.forms import CreateUserForm
from online_library_django_template_project.profile_app.models import UserProfile


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = UserProfile
    form_class = EditUserForm
    template_name = 'edit-profile.html'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse_lazy('details-profile', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'delete-profile.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = EditUserForm(instance=self.request.user.userprofile)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
        return self.render_to_response(self.get_context_data(form=form))

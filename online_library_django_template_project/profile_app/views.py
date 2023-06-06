from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from online_library_django_template_project.profile_app.forms import EditUserForm, DeleteUserForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteUserForm(instance=self.object.userprofile)
        return context

from django.shortcuts import render, redirect

from online_library_django_template_project.library_app.forms import UploadBookForm
from online_library_django_template_project.profile_app.models import UserProfile


# Create your views here.

def add_book(request):
    form = UploadBookForm()
    context = {'form': form, 'profile': UserProfile.objects.first()}

    if request.method == "POST":
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-book')

    return render(request=request, template_name='add-book.html', context=context)

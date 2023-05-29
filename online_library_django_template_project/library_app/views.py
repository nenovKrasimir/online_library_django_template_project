from django.shortcuts import render, redirect
from django.views import View

from online_library_django_template_project.library_app.forms import UploadBookForm, EditBookForm
from online_library_django_template_project.library_app.models import Book
from online_library_django_template_project.profile_app.models import UserProfile


# Create your views here.
class AddBookView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile = UserProfile.objects.first()

    def get(self, request):
        form = UploadBookForm()
        context = {'form': form, 'profile': self.profile}
        return render(request=request, template_name='add-book.html', context=context)

    def post(self, request):
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = self.profile
            book.save()
            return redirect('home-page')


def details_book(request, pk):
    profile = UserProfile.objects.first()
    book = Book.objects.filter(id=pk).first()
    context = {'book': book, 'profile': profile}
    return render(request=request, template_name='book-details.html', context=context)


def edit_book(request, pk):
    profile = UserProfile.objects.first()
    book = Book.objects.filter(id=pk).first()
    form = EditBookForm(instance=book)
    context = {'book': book, 'profile': profile, 'form': form}

    if request.method == 'POST':
        book_for_edit = EditBookForm(request.POST, request.FILES, instance=book)

        if book_for_edit.is_valid():
            book_for_edit.save()
            return redirect('home-page')

    return render(request=request, template_name='edit-book.html', context=context)


def delete_book(request, pk):
    book = Book.objects.filter(id=pk).first()
    book.delete()
    return redirect('home-page')

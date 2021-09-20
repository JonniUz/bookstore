from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import ReviewForm, CategoryForm, AuthorForm, BookForm
from .models import Category, Book


class BookListView(ListView):
    model = Book
    template_name = 'books/index.html'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title']
    template_name = 'books/index.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)
    success_url = 'success'

def success(request):
    return render(request, 'books/success.html')
'''


@login_required
def index(request):
    form = CategoryForm()
    if request.method == "POST":
        newCategory = Category(user=request.user)
        form = CategoryForm(request.POST, instance=newCategory)
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request, 'books/index.html', {'form': form})


'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from library.models import *
from library.forms import *


# Create your views here.

#_________________________AUTHOR_________________________________

@login_required
def author_create(request):

    form = AuthorForm()

    if request.method == 'POST':

        form = AuthorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Author profile has been created successfully.')

            return redirect('author_list')  
        
    context = {
        'form':form
    }    

    return render(request, 'library/authors/author_create.html', context)

def author_list(request):

    a_data = AuthorModel.objects.all()

    context = {
        'a_data':a_data
    }

    return render(request, 'library/authors/author_list.html', context)

def author_details(request, a_id):

    a_data = get_object_or_404(AuthorModel, id=a_id)
    
    context = {
            'a_data':a_data
        }

    return render(request, 'library/authors/author_details.html', context)

def author_update(request, a_id):

    a_data = get_object_or_404(AuthorModel, id=a_id)

    form = AuthorForm(instance=a_data)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=a_data)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    
        context = {
            'form': form,
            'a_data': a_data
            }
    
    return render(request, 'library/authors/author_update.html', context)

@login_required
def author_delete(request, a_id):

    a_data = get_object_or_404(AuthorModel, id=a_id)

    a_data.delete()

    messages.success(request, 'Author deleted successfully.')

    return redirect('author_list')


#_________________________BOOKS_________________________________


def book_create(request):

    form = BookForm()

    if request.method == 'POST':

        form = BookForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, 'Book has been published.')

            return redirect('book_list')

    context = {
        'form': form
    }    

    return render(request, 'library/books/book_create.html', context)

def book_list(request):

    b_data = BookModel.objects.all()

    context = {
        'b_data':b_data
    }
    return render(request, 'library/books/book_list.html', context)

def book_details(request, b_id):

    b_data = get_object_or_404(BookModel, id=b_id)

    context = {
        'b_data':b_data
    }
    return render(request, 'library/books/book_details.html', context)

@login_required
def book_update(request, b_id):

    b_data = get_object_or_404(BookModel, id=b_id)

    form = BookForm(instance=b_data) 

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=b_data)
        if form.is_valid():
            form.save()

            messages.success(request, 'Updated Book Info Successfully.')

            return redirect('book_list')

    context = {
        'form': form,
        'b_data': b_data
    }    

    return render(request, 'library/books/book_update.html', context)

@login_required
def book_delete(request, b_id):

    b_data = get_object_or_404(BookModel, id=b_id)

    b_data.delete()

    messages.success(request, 'Book deleted successfully.')

    return redirect('book_list')



#_________________________BORROW RECORD_________________________________


def borrow_create(request):

    form = BorrowRecordForm()

    if request.method == 'POST':

        form = BorrowRecordForm(request.POST)

        if form.is_valid():
            borrow_record = form.save(commit=False)
            borrow_record.user = request.user
            borrow_record.save()

            messages.success(request, 'Borrowed Successfully')

            return redirect('borrow_list')

    context = {
        'form':form
    }    
        
    return render(request, 'library/borrow/borrow_create.html', context)

def borrow_list(request):

    br_data = BorrowRecordModel.objects.all()

    context = {
        'br_data': br_data
    }
    return render(request, 'library/borrow/borrow_list.html', context)

def borrow_details(request, br_id):

    br_data = get_object_or_404(BorrowRecordModel, id = br_id)

    context = {
        'br_data':br_data
    }    
    return render(request, 'library/borrow/borrow_details.html', context)

def borrow_update(request, br_id):

    br_data = get_object_or_404(BorrowRecordModel, id = br_id)
    
    form = BorrowRecordForm(instance=br_data)
    
    if request.method == 'POST':
    
        form = BorrowRecordForm(request.POST, instance=br_data)
    
        if form.is_valid():
            form.save()
    
            messages.success(request, 'Updated Borrowed Book Information.')
    
            return redirect('borrow_list')
    
        context = {
            'form':form,
            'br_data':br_data
        }    
    

    return render(request, 'library/borrow/borrow_update.html', context)

@login_required
def borrow_delete(request, br_id):

    br_data = get_object_or_404(BorrowRecordModel, id=br_id)

    br_data.delete()

    messages.success(request, 'Borrow record deleted successfully.')

    return redirect('borrow_list')


#_________________________CATEGORIES_________________________________


def category_create(request):

    form = CategoryForm()

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Category Created.')

            return redirect('category_list')

    context = {
        'form': form
    }    
    return render(request, 'library/categories/category_create.html', context)

def category_list(request):

    c_data = CategoryModel.objects.all()

    context = {
        'c_data':c_data
    }
    return render(request, 'library/categories/category_list.html', context)

def category_details(request, c_id):

    c_data = get_object_or_404(CategoryModel, id = c_id)
    
    context = {
            'c_data':c_data
        }
    return render(request, 'library/categories/category_details.html', context)

def category_update(request, c_id):

    c_data = get_object_or_404(CategoryModel, id = c_id)

    form = CategoryForm(instance=c_data)
    
    if request.method == 'POST':
    
        form = CategoryForm(request.POST, instance=c_data)
    
        if form.is_valid():
            form.save()
    
            messages.success(request, 'Category Updated.')
    
            return redirect('category_list')

    context ={
        'form':form,
        'c_data':c_data
    }    

    return render(request, 'library/categories/category_update.html', context)

@login_required
def category_delete(request, c_id):

    c_data = get_object_or_404(CategoryModel, id=c_id)

    c_data.delete()

    messages.success(request, 'Category deleted successfully.')

    return redirect('category_list')
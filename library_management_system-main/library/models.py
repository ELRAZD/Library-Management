from django.db import models
from django.conf import settings


# Create your models here.


class AuthorModel(models.Model):

    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unknown Author"


class CategoryModel(models.Model):

    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Category"


class BookModel(models.Model):

    title = models.CharField(max_length=150)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    available_quantity = models.PositiveIntegerField(default=1)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BorrowRecordModel(models.Model):

    STATUS = [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrow_records')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='borrow_records')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Borrowed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular department instance.
        """
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular department instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "author"

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        """
        Returns the url to access a particular department instance.
        """
        return reverse('publisher-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"

class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="books")
    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this employee.
        """
        return reverse('book-detail', args=[str(self.id)])

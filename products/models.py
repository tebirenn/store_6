from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)  
    # category_id

    def __str__(self):
        return self.name
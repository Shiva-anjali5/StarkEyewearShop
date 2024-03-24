from django.db import models

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

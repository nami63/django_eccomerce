from django.db import models

# products
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'live'), (DELETE, 'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')  # corrected upload_to path
    priority = models.IntegerField(default=0)
    delete_status = models.DateTimeField(auto_now_add=True)
    create_status = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

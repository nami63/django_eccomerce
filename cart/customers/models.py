from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'live'), (DELETE, 'Delete'))

    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=10)
    delete_status = models.DateTimeField(auto_now_add=True)
    create_status = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

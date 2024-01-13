from django.db import models

class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='media/site')
    caption = models.TextField()

    def some_method(self):
        # Your method logic here
        pass

    def __str__(self):
        return f"Site Settings - {self.caption}"

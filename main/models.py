from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    published = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return f"{self.title} - {self.published.strftime('%d/%m/%Y')} - {self.text[:30]}"
    
from django.db import models


class faq(models.Model):

    question = models.TextField(blank=True, default='')
    answer = models.TextField(blank=True, default='')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.question

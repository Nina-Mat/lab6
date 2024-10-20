from  django.contrib.auth.models import  User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE);

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > 300:
            return self.text[: 300]
        else:
            return self.text
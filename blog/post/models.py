from django.db import models

from django.conf import settings




class Post(models.Model):

    title = models.CharField(max_length=230)
    date  = models.DateField()
    image = models.ImageField(upload_to='media/')
    body  = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)


    def __str__ (self):

          return  self.title





    def summary(self):
        return self.body[:150]

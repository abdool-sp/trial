from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Data(models.Model):
    User            =   models.ForeignKey(User,on_delete=models.CASCADE)
    heart_rate      =   models.IntegerField(default=0)
    temperature     =   models.IntegerField(default=0)
    timestamp       =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.User.username
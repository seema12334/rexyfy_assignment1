from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tasks(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    tilte= models.CharField(max_length=200)
    description= models.TextField(max_length=1000)
    create= models.DateTimeField(auto_now_add=True)
    # taskshare= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tilte
    
    class Meta:
        ordering = ['create']
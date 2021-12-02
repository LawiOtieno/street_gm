from django.db import models
from authentication.models import User, AbstractUser
from helpers.models import TrackingModel

# Create your models here.

class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

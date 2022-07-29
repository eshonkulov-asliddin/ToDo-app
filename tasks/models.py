
from django.db import models
import uuid
from users.models import Profile
from django.forms import CharField


# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    class Meta:
        ordering = ['completed', '-date']

        # @property
        # def countTasks(self):
        #     tasks = self.all()
        #     incomplete = tasks.filter(completed=False)
    
        
    def __str__(self) -> str:
        return self.name
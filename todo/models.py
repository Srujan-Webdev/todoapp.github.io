from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(User, null=True, default=True, on_delete=models.CASCADE)
    
    #Adding below date picker for sending reminders mail to complete the task
    time_tobe_completed = models.DateField()

    # To display the items in latest ones first order
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content

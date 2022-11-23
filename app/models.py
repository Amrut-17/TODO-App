from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# create table which contains :
# user - foreign key from user
# title
# completion status
# task pririty
# created date

class TODO(models.Model):
    title = models.CharField(max_length=50)

    # list for completion status
    completion_status = [
        ('C', 'COMPLETE'),
        ('P', 'PENDING'),
        ('F', 'FAILED'),
    ]
    status = models.CharField(max_length=2, choices=completion_status)

    # task priority between 1 to 5
    priority_status = [
        ('1','Very Low'),
        ('2','Low'),
        ('3','Medium'),
        ('4','High'),
        ('5','Very High'),
    ]
    priority = models.CharField(max_length=2, choices=priority_status)
    
    created_at = models.DateTimeField(auto_now_add=True)

    # the list of user from user_auth table : Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  (self.title + " --Stautus--> " +self.status)
    


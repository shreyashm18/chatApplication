from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Participants(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.user.first_name

    @property
    def room(self):
        return self.rooms_set.all()
        
class Rooms(models.Model):
    
    # Room title
    title = models.CharField(max_length=255)
    group_members = models.ManyToManyField(User) 

    # If only "staff" users are allowed (is_staff on django's User)
    # staff_only = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    


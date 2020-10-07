from django.contrib import admin

# Register your models here.
from .models import Participants,Rooms

admin.site.register(Participants)
admin.site.register(Rooms)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GroupForm
from django.contrib.auth.decorators import login_required
from .models import Rooms
from django.contrib.auth.models import User,auth

# Create your views here.
def showchathome(request):
    return HttpResponse('chat Home')

def chatpage(request, room, user):
    # return HttpResponse('chat page '+room + ' ' +user)
    member = User.objects.get(first_name= user)
    groups = member.rooms_set.all()
    print(groups)
    
    
    if groups.filter(title=room).exists():
        return render(request, 'chat_screen.html' , {'room_name':room , 'person_name':user})
    else:
        return render(request,'check.html')

@login_required(login_url = 'user_login')
def create_group(request):
    add=GroupForm()
    if request.method=='POST':
        add=GroupForm(request.POST)
        if add.is_valid():
            add.save()
            return redirect('home')
    else:
        return render(request, 'create_group.html', {'upload_form':add})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GroupForm, addOrRemoveMember
from django.contrib.auth.decorators import login_required
from .models import Rooms
from django.contrib.auth.models import User,auth

# Create your views here.
def showchathome(request):
    return HttpResponse('chat Home')

@login_required(login_url = 'user_login')
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

def changeMember(request, room_name = None, person_name = None):
    print(room_name)
    # room_name=str(room_name)
    
    try:
        room = Rooms.objects.get(title = room_name)
    except Rooms.DoesNotExist:
        return redirect('home')
    admin = room.admin
    print(admin)
    if(person_name == str(admin)):
        change_member=addOrRemoveMember(request.POST or None, instance=room)
        if change_member.is_valid():
            change_member.save()
            return render(request, 'chat_screen.html',{'room_name':room_name , 'person_name':person_name})
        return render(request, 'addOrRemovemember.html', {'upload_form':change_member,})
    else:
        return render(request,'notAdmin.html')

# def update_prod(request,prod_id):
#     print(type(prod_id))
#     prod_id=int(prod_id)
#     try:
#         product=Products.objects.get(id=prod_id)
#     except Products.DoesNotExist:
#         return redirect('all_products')
#     title_string = f"Edit {product.product_name} information"
#     prod_edit=ProductForm(request.POST or None, instance=product)
#     if prod_edit.is_valid():
#         prod_edit.save()
#         return redirect('all_products')
#     return render(request, 'product_add.html', {'upload_form':prod_edit,"title":title_string,})
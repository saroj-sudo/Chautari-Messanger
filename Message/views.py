from django.shortcuts import render,redirect
from django.db.models import Q
from .models import *
from django.contrib.auth.models import User

def chatroom(request,id):
    if request.method=='POST':
       if request.POST['body']:
           new_message=Message()
           new_message.body=request.POST['body']
           new_message.sender=request.user.id
           new_message.receiver=id
           new_message.save()
           return redirect('/message/message/'+str(id))

    messages=Message.objects.filter(Q(sender=request.user.id,receiver=id)|Q(sender=id,receiver=request.user.id))
    for message in messages:
        message.user=User.objects.get(id=message.sender)
        if message.user.id==request.user.id:
            message.truth_value=True
    arko_ko_name=User.objects.get(id=id)

    return render(request,'chatroom.html',{'messages':messages,'arko_ko_name':arko_ko_name})
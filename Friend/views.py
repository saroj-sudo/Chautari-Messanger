from django.shortcuts import render
from Friend.models import Friend
from django.db.models import Q
from django.contrib.auth.models import User
def friend_list(request):
    friend_table=Friend.objects.filter(Q(sender=request.user.id)|Q(receiver=request.user.id))
    for friend in friend_table:
        if friend.receiver==request.user.id:
            friend.id=friend.sender
        else:    
            friend.id = friend.receiver
        friend.user=User.objects.get(id=friend.id)
    return render(request,'friend_list.html',{'friend':friend_table})
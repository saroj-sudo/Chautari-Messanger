from django.shortcuts import render,redirect
from Post.models import Post,Comment,Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Friend.models import Friend
from django.db.models import Q



# Create your views here.
@login_required(login_url='/login')
def show_post(request):
    posts = Post.objects.all().order_by('-date')
    for post in posts:
        post.like=Like.objects.filter(post=post).count()
        try:
                Like.objects.get(user=request.user,post=post)
                post.is_liked=True
        except:
                pass
        post.usr=User.objects.get(id=post.user.id)
        post.cmt=Comment.objects.filter(post=post)
        for cmt in post.cmt:
            post.cmt.commentor=User.objects.get(id=cmt.commentor.id)
        
        friend_table=Friend.objects.filter(Q(sender=request.user.id)|Q(receiver=request.user.id))
        for friend in friend_table:
                if friend.receiver==request.user.id:
                        friend.id=friend.sender
                else:    
                        friend.id = friend.receiver
                friend.user=User.objects.get(id=friend.id)
    return render(request,'home.html',{'posts':posts,'friend':friend_table})
@login_required(login_url='/login')
def new_post(request):
        if request.method=='POST':
                new_post=Post()
                new_post.body=request.POST['body']
                new_post.user=request.user
                new_post.save()
                return redirect('/')
        return render(request,'new_post.html')
@login_required(login_url='/login')
def save_comment(request,id):
        if request.POST['body']:
                new_comment=Comment()
                new_comment.body=request.POST['body']
                new_comment.commentor=request.user
                new_comment.post=Post.objects.get(id=id)
                new_comment.save()
                return redirect('/')

@login_required(login_url='/login')
def like(request,id):
        if request.method=="POST":
                try:
                        nlike=Like.objects.get(user=request.user,post=Post.objects.get(id=id))
                        nlike.delete()
                        
                except:
                        new_like=Like()
                        new_like.user=request.user
                        new_like.post=Post.objects.get(id=id)
                        new_like.save()
                return redirect('/')




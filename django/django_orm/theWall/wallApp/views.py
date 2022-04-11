
from django.shortcuts import redirect, render
from app import views
from wallApp.models import User,Message,Comment


def index(request):
    user=User.objects.filter(email=request.session['email'])
   
    context={
        'user':user[0],
        'messages': Message.objects.all(),
        

    }
    return render(request,'wall.html',context)
def addpost(request):
    post=request.POST['post']
    user=User.objects.get(email=request.session['email'])
    Message.objects.create(message=post,user=user)
    return redirect('/sucsess')

def addcomment(request,userid,mid):
    comment= request.POST['comment']
    message = Message.objects.get(id=mid)
    user =User.objects.get(id=userid)
    Comment.objects.create(comment=comment,message=message,user=user)
    return redirect('/sucsess')
    
    



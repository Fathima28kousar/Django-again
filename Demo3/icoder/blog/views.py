from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from .models import Post,Blogcomment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras

def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= Blogcomment.objects.filter(post=post, parent=None)
    replies= Blogcomment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = get_object_or_404(Post, sno=postSno)  # Handle Post object retrieval
        parentSno = request.POST.get('parentSno')

        # Check if parentSno is provided
        if parentSno:
            parent_comments = Blogcomment.objects.filter(sno=parentSno)
            if len(parent_comments) == 0:
                # Handle the case where the parent Blogcomment doesn't exist
                messages.error(request, "The parent comment does not exist.")
                return redirect(f"/blog/{post.slug}")

            parent = parent_comments[0]  # Since there should be only one parent comment
            comment = Blogcomment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        else:
            # No parentSno provided, so it's a top-level comment
            comment = Blogcomment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        
        return redirect(f"/{post.slug}")
    else:
        # Handle GET requests
        return HttpResponse('404 Not Found')

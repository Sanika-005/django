# from selectors import EpollSelector
from lib2to3.pgen2.token import GREATER, GREATEREQUAL
from select import select
from django.shortcuts import render,redirect,get_object_or_404
from django.template import context
from .models import PostModel,Comment
from .forms import PostModelForm,PostUpdateForm,CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm
    form = PostModelForm()
    context = {
        'posts':posts,
        'form':form
    }
    return render(request, 'blog/index.html', context)

def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    print(post)
    p = PostModel.objects.get(id=pk)
    comments = p.comment_set.all()
    # user = request.user
    # print(user)
    comments = Comment.objects.all()
    print(comments)
    stuff = get_object_or_404(PostModel,id=pk)
    total_likes = post.total_likes
    context={
        'comments':comments,
        'total_likes':total_likes
    }
    # stuff = get_object_or_404(PostModel,id=request.kwargs['pk'])
    # total_likes = stuff.total_likes()
    context["total_likes"] = total_likes
    context={
        'comments':comments,
        'total_likes':total_likes
    }
    if context["total_likes"] is GREATEREQUAL :
        print("hrllo")
        return render(request,'blog/post_detail.html',context)
    # instance = get_object_or_404(PostModel,pk=pk)
    # content_type = ContentType.objects.get_for_model(PostModel)
    # obj_id = instance.id
    # comms = Comment.objects.filter(content_type=content_type,object_id=obj_id)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        # r_form = ReplyToComments(request.POST)
        if c_form.is_valid():
            # try:
            #     parent_id = int(request.POST.get("parent_id"))
            # except:
            #     parent_id = None

            # if parent_id:
            #     parent_qs = Comment.objects.filter(parent__id=parent_id)
            #     if parent_qs.exists() and parent_qs.count==1:
            #         parent_obj = parent_qs.first()
            instance = c_form.save(commit=False)
            # rinstance = r_form.save(commit=False)
            instance.user = request.user
            # rinstance.user = request.user
            instance.post = post
            # rinstance.post = post
            instance.save()
            # rinstance.save()
            # stuff = get_object_or_404(PostModel,id=self.kwargs['pk'])
            return redirect('blog-post-detail',pk=post.id)
    else:
        c_form = CommentForm()
        post = PostModel.objects.get(id=pk)
        total_likes = post.total_likes
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True
        # r_form = ReplyToComments()
    context = {
        'comments':comments,
        'post':post,
        'c_form':c_form,
        'total_likes':total_likes,
        'liked':liked
    }
    print(post)
    return render(request,'blog/post_detail.html',context)   

def post_edit(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail',pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request,'blog/post_edit.html',context)   

def post_delete(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post':post
    }
    return render(request,'blog/post_delete.html',context)

def LikeView(request,pk):
    post = get_object_or_404(PostModel,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog-post-detail', args=[str(pk)]))
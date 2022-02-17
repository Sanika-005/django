from multiprocessing import parent_process
from pyexpat import model
from select import select
from statistics import mode
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()

    def total_likes(self):
        return self.likes.count()

    def comments(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.title
    
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager,self).filter(parent=None)
        return qs

    def filetr_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager,self).filter(content_type=content_type,object_id=obj_id,parent=None)
        return qs

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True,blank=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey('content_type','object_id')
    
    def __str__(self):
        return self.content

    def name(self):
        return self.user

    def children(self):#replies
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class userinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) #it is a onetoone link to the User table which is made by default.
    birthday=models.DateField(default=timezone.now) #timezone.now helps us to take the current date.
    gender=models.CharField(default="M",max_length=8) #max_length is a necessary argument.
    about=models.CharField(max_length=200 , blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures/', blank = True)
    cover_pic = models.ImageField(upload_to='cover_pictures/', blank = True)

    def __str__(self):
        return self.user.first_name

class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_info = models.ForeignKey(userinfo,on_delete=models.CASCADE ,null=True)
    photo=models.ImageField(upload_to='postimages/', null = True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    text=models.CharField(max_length=500,blank=True)
    l=models.IntegerField(default=0)
    c=models.IntegerField(default=0)
    time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first_name

class likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_info =  models.ForeignKey(userinfo,on_delete=models.CASCADE ,null=True)
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    cmnt=models.CharField(max_length=100,blank=True)
    time=models.DateTimeField(default=timezone.now )

    def __str__(self):
        return self.user.first_name

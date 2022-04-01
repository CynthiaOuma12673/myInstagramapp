from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, default='My Bio', blank=True)
    name = models.CharField(blank=True, max_length=150)
    profile_pic = CloudinaryField('profile_pic')

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=150, blank=True)
    caption = models.CharField('Caption(optional)', max_length=400, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-upload_date']

    
    def __str__(self):
        return f'{self.user.username} Image'
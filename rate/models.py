from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles',blank=True)
    # user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
    bio=models.TextField(blank=True,null=True)
    contact=models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()



class Project(models.Model):
    title=models.CharField(max_length =30)
    image=models.ImageField(upload_to ='projects/', blank = True)
    description=models.TextField(blank=True,null=True)
    # profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # link=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()

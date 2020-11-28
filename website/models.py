from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#The user 
class User(AbstractUser):
    pass

class Class_Room(models.Model):
    
    
    name=models.CharField(verbose_name="Room name",max_length=40)
    description=models.TextField(verbose_name="Room description",max_length=400)

    id=models.AutoField(verbose_name="Primary Key",primary_key=True)    
    link_suffix=models.CharField(verbose_name="room link suffix",max_length=7)
    creator_id=models.IntegerField(verbose_name="ID of room creator")
    creation_date=models.DateField(verbose_name="date of creation",default=None)
    

class Group_Member():
    pass

class Calendar(models.Model):
    #references the class room
    class_room=models.ForeignKey(Class_Room,on_delete=models.CASCADE)

class Day(models.Model):
    calendar=models.ForeignKey(Calendar,on_delete=models.CASCADE)


class Exam(models.Model):
    description=models.TextField(verbose_name="What are the topics",max_length=5000)


class Homework(models.Model):
    day=models.ForeignKey(Day,on_delete=models.CASCADE)

class HW_Subject(models.Model):
    #refs it's homework object/instance
    homework=models.ForeignKey(Homework,on_delete=models.CASCADE)

    description=models.TextField(verbose_name="listing stuff todo")
    lessson_name=models.CharField(verbose_name="lesson, eg. English",max_length=200)
    creation_date=models.DateField()


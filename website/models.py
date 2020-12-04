from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils

# Create your models here.


#The user 
class User(AbstractUser):
    pass

class GroupMember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        permissions=(
            ("is_admin","User is Admin or not"),
            ("edit_content","User may edit content"),
            ("delete_content","User may delete content"),
            ("add_content","User may add content"),
            ("upload_image","User may upload images"),
            ("edit_room","User may change room settings")
        )

class Class_Room(models.Model):
    
    
    name=models.CharField(verbose_name="Room name",max_length=40)
    description=models.TextField(verbose_name="Room description",max_length=400)

    id=models.AutoField(verbose_name="Primary Key",primary_key=True)    
    link_suffix=models.CharField(verbose_name="room link suffix",max_length=7)
    creator_id=models.IntegerField(verbose_name="ID of room creator")
    creation_date=models.DateTimeField(verbose_name="date of creation",auto_now_add=True)
    members=models.ManyToManyField(GroupMember)
    room_icon=models.ImageField(default=None)

    def __str__(self):
        return self.name

class Calendar(models.Model):
    #references the class room
    class_room=models.ForeignKey(Class_Room,on_delete=models.CASCADE)

class Day(models.Model):
    calendar=models.ForeignKey(Calendar,on_delete=models.CASCADE)


class Exam(models.Model):
    day=models.ForeignKey(Day,on_delete=models.CASCADE,default=None)
    description=models.TextField(verbose_name="Exam topics",max_length=5000)
    

    SUBJECT_CHOICES=(
        ("Englisch","Englisch"),
        ("Deutsch","Deutsch"),
        ("Mathe","Mathe"),
        ("Französisch","Französisch"),
        ("Latein","Latein"),
        ("Spanisch","Spanisch"),
        ("Physik","Physik"),
        ("Chemie","Chemie"),
        ("Biologie","Biologie"),
        ("Erdkunde","Erdkunde"),
        ("Kunst","Kunst"),
        ("Musik","Musik"),
        ("Powi","Powi"),
        ("Geschichte","Geschichte"),
        ("Sport","Sport"),
        ("Evangelisch","Evangelisch"),
        ("Katholisch","Katholisch"),
        ("Ethik","Ethik"),
        ("LSD","LSD"),
        ("Informatik","Informatik"),
        ("Cambridge","Cambridge"),
        ("NaWi","NaWi")
    )

    subject = models.CharField(max_length=100,choices=SUBJECT_CHOICES,default="Englisch")

class Exam_File(models.Model): #enctype="multipart/form-data" in form field
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    data_file=models.FileField(upload_to="website/media")


class Homework(models.Model):
    day=models.ForeignKey(Day,on_delete=models.CASCADE)
    creation_date=models.DateTimeField(default=django.utils.timezone.now)
    

class HW_Subject(models.Model):
    #refs it's homework object/instance
    homework=models.ForeignKey(Homework,on_delete=models.CASCADE)

    description=models.TextField(verbose_name="listing stuff todo")
    lessson_name=models.CharField(verbose_name="lesson, eg. English",max_length=200)
    creation_date=models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User


# django auto increments Primary Keys.
# So the first student/user will have an auto ID of #1.
# Same as the admin and so on for every other database table.
class user(models.Model):
    SKILLS_CHOICES = [('Beginner','Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')]
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=False)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skill_level = models.CharField(choices=SKILLS_CHOICES,max_length=12, blank=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.user.username

class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=18)

class instrument(models.Model):
    instrument_name = models.CharField(max_length=250)
    instrument_category = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)

class teacher(models.Model):
    name = models.CharField(max_length=250, null=False)
    room = models.IntegerField(null=False)

class schedule(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    Instrument = models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Lesson_id = models.CharField(max_length=100, null=False)
    Language = models.CharField(max_length=100)

class bookings(models.Model): #shows student's bookings
	student = models.ForeignKey(user, on_delete=models.CASCADE)
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
	schedule = models.ForeignKey(schedule, on_delete=models.CASCADE)

class invoice(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	receipt = models.IntegerField(null=False)

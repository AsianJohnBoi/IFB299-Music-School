from django.db import models

# django auto increments Primary Keys.
# So the first student/user will have an auto ID of #1.
# Same as the admin and so on for every other database table.
class user(models.Model):
    SKILLS_CHOICES = [('Beginner','Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')]
    GENDER_CHOICES = [('M', 'Male'),('F', 'Femail')]
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=18)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    age = models.IntegerField(null=False)
    submittion_date = models.DateTimeField()
    skill_level = models.CharField(choices=SKILLS_CHOICES,max_length=12, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=False)

class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=18)

class instrument(models.Model):
    instrument_name = models.CharField(max_length=250)
    instrument_category = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)

# class hire(models.Model):

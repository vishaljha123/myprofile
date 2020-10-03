from django.db import models
from phone_field import PhoneField
# Create your models here.

class Userinfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_add = models.EmailField()
    phone = PhoneField(primary_key=True)
    position = models.CharField(max_length=255)

    education = models.CharField(max_length=255)

    work_exp = models.FloatField()
    resume = models.FileField(upload_to='static/')

    video_resume = models.FileField(upload_to='media/')




    def __str__(self):
        return self.first_name, self.last_name


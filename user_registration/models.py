# userregistration/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import FileExtensionValidator

from django.db import models
from django.contrib.auth.models import AbstractUser

class ClassModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
     # image = models.ImageField(upload_to='profile_images/', blank=True, null=True,
    #                           validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    facebookProfile = models.URLField(blank=True, null=True)
    instaProfile = models.URLField(blank=True, null=True)
    twitterProfile = models.URLField(blank=True, null=True)
    isTeacher = models.BooleanField(default=False)
    myClasses = models.ManyToManyField('ClassModel', related_name='enrolled_users', blank=True)
    myCourses = models.ManyToManyField('Course', related_name='enrolled_users', blank=True)

    def __str__(self):
        return self.name



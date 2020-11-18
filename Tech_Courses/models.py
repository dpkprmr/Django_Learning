from django.db import models

# Create your models here.

class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    instructorname = models.CharField(max_length=100)
    def __str__(self):
        return self.coursename

class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    self_paced = models.CharField(max_length=500)
    instructor_lead = models.CharField(max_length=500)
    def __str__(self):
        return self.self_paced

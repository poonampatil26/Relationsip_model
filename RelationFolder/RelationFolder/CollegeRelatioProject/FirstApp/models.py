from django.db import models

# Create your models here.

class Department(models.Model):
    dept=models.CharField(max_length=100)


    def __str__(self):
        return self.dept


class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    dob=models.DateField()
    dept_stu = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    dept_lect = models.ManyToManyField(Department)
    lecturer = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):  #repr
        return self.lecturer

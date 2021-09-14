from django.contrib import admin
from .models import Student, Department, Lecturer

class StudentAdmin(admin.ModelAdmin):
    list = ['id','name','email','dob','dept_stu']

admin.site.register(Student,StudentAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list = ['id', 'dept']

admin.site.register(Department, DepartmentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list = ['id', 'lecturer', 'email','dept_lect']

admin.site.register(Lecturer, LecturerAdmin)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Department, Lecturer
from .forms import StudentForm, DepartmentForm, LecturerForm
from django.contrib import messages

def add_stu(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
    template_name = 'FirstApp/add_stu.html'
    context = {'form':form}
    return render(request, template_name, context)

def show_stu(request):
    info = Student.objects.all()
    template_name = 'FirstApp/show_stu.html'
    context = {'info':info}
    return render(request, template_name, context)

def update_stu(request, id_f):
    info = Student.objects.get(id=id_f)
    form = StudentForm(instance=info)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
    template_name = 'FirstApp/add_stu.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_stu(request, id_f):
    info = Student.objects.get(id=id_f)
    info.delete()
    return redirect('show_stu')


# -------------------------------------------------------------------------------------------------------------------


def add_lect(request):
    form = LecturerForm()
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lect')
    template_name = 'FirstApp/add_lect.html'
    context = {'form':form}
    return render(request, template_name, context)

def show_lect(request):
    info = Lecturer.objects.all()
    template_name = 'FirstApp/show_lect.html'
    context = {'info':info}
    return render(request, template_name, context)

def update_lect(request, id_f):
    info = Lecturer.objects.get(id=id_f)
    form = LecturerForm(instance=info)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('show_lect')
    template_name = 'FirstApp/add_lect.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_lect(request, id_f):
    info = Lecturer.objects.get(id=id_f)
    info.delete()
    return redirect('show_lect')


#------------------------------------------------------------------------------------------------------------

def add_dpt(request):
    records = Department.objects.all()
    print(records)
    flag = 'Not Available'
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            for i in records:
                if i.dept == form.cleaned_data['dept']:
                    flag = 'Record already exist'
                    return HttpResponse(f'{flag}')
            form.save()
            return redirect('show_dpt')
    template_name = 'FirstApp/add_dpt.html'
    context = {'form':form}
    return render(request, template_name, context)

def show_dpt(request):
    info = Department.objects.all()
    template_name = 'FirstApp/show_dpt.html'
    context = {'info':info}
    return render(request, template_name, context)

def update_dpt(request, id_f):
    info = Department.objects.get(id=id_f)
    form = DepartmentForm(instance=info)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('show_dpt')
    template_name = 'FirstApp/add_dpt.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_dpt(request, id_f):
    info = Department.objects.get(id=id_f)
    data = Lecturer.objects.filter(dept_lect=info)
    for i in data:
        for j in i.dept_lect.all():
            if len(i.dept_lect.all()) == 1 and j == info:
                i.delete()
    info.delete()
    return redirect('show_dpt')


#---------------------------------------------------------------------------------------------------------------------

def home(request):
    template_name = 'FirstApp/home.html'
    context = {}
    return render(request, template_name, context)


def search(request):
    print('get form')
    if request.method=='POST':
        srch=request.POST.get('searchkey')
        print(srch)
        record=Student.objects.filter(name=srch)
        print(record)
        recordlect=Lecturer.objects.filter(lecturer=srch)
        print(recordlect)
        context={'record':record,'recordlect':recordlect}

        return render(request,'FirstApp/showresult.html',context)

    template_name='FirstApp/search.html'
    context={}
    return render(request, template_name, context)


def search_dept_stu(request,id):
    data=Department.objects.get(id=id)
    record=Student.objects.filter(dept_stu=data)
    print(record)
    template_name='FirstApp/showdeptstudent.html'
    context={'record':record}
    return render(request, template_name, context)

def search_dept_lect(request,id):
    data = Department.objects.get(id=id)
    record = Lecturer.objects.filter(dept_lect=data)
    print(record)
    template_name = 'FirstApp/showdeptlect.html'
    context = {'record': record}
    return render(request, template_name, context)

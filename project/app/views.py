from django.shortcuts import render
from .models import Department,Student
from .forms import StudentForm,DepartmentForm
from django.db.models import Q



# Create your views here.
def home(request):
    stu_form = StudentForm()
    dep_form = DepartmentForm()
    return render(request,'app/home.html',{'stu_form':stu_form,'dep_form':dep_form})

def add_dep(request):
    if request.method=="POST":
        dep_name = request.POST.get('dep_name')
        description = request.POST.get('description')
        data = Department.objects.filter(dep_name=dep_name)
        if data:
            msg = "Department Already exist"
            stu_form = StudentForm()
            dep_form = DepartmentForm()
            return render(request,'app/home.html',{'msg':msg,'stu_form':stu_form,'dep_form':dep_form})
        else:
            Department.objects.create(dep_name=dep_name,
                                           description=description)
            msg = "Department Created Successfully"
            stu_form = StudentForm()
            dep_form = DepartmentForm()
            return render(request,'app/home.html',{'msg':msg,'stu_form':stu_form,'dep_form':dep_form})

def add_stu(request):
    if request.method=='POST':
        stu_name=request.POST.get('stu_name')
        stu_class=request.POST.get('stu_class')
        stu_department=request.POST.get('stu_department')
        stu_email=request.POST.get('stu_email')
        stu_mobile=request.POST.get('stu_mobile')
        # data = Student.objects.filter(Q(stu_department=stu_department) & Q(stu_email=stu_email))
        data = Student.objects.filter(stu_email=stu_email)
        if data:
            if data.stu_department_id:
                msg1 = "Student already register in department"
                stu_form = StudentForm()
                dep_form = DepartmentForm()
                return render(request,'app/home.html',{'msg':msg1,'stu_form':stu_form,'dep_form':dep_form})
            else:
                data = Department.objects.get(id=stu_department)
                Student.objects.create(stu_name=stu_name,
                                            stu_class=stu_class,
                                            stu_department=data,
                                            stu_email=stu_email,
                                            stu_mobile=stu_mobile)
                msg2 = "Student Registration Successfully"
                stu_form = StudentForm()
                dep_form = DepartmentForm()
                return render(request,'app/home.html',{'msg':msg2,'stu_form':stu_form,'dep_form':dep_form})
        else:
                data = Department.objects.get(id=stu_department)
                Student.objects.create(stu_name=stu_name,
                                            stu_class=stu_class,
                                            stu_department=data,
                                            stu_email=stu_email,
                                            stu_mobile=stu_mobile)
                msg2 = "Student Registration Successfully"
                stu_form = StudentForm()
                dep_form = DepartmentForm()
                return render(request,'app/home.html',{'msg':msg2,'stu_form':stu_form,'dep_form':dep_form})
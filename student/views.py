from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import reg, employee
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'reg.html')


def saveform(request):
    if request.method == "POST":
        obj = reg(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            contact=request.POST['mobile'],
            address=request.POST['address']
        )
        obj.save()
        messages.success(request, "Registration Completed Successfully!")
        #return redirect('reg')
    else:
        messages.warning(request, "Registration Failed!")
        #return redirect("/")
        #return HttpResponse("Registration Completed Successfully!")

    #return render(request, "reg.html")


def viewstudent(request):
    data = reg.objects.all()
    return render(request, "viewstudent.html", {'data': data})


# Delete Student
def deletestudent(request, id):
    student = reg.objects.get(id=id)
    student.delete()
    return redirect('viewstudent')


# Update Student
def updatestudent(request, id):
    student = reg.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.password = request.POST['password']
        student.contact = request.POST['mobile']
        student.address = request.POST['address']  # typo fixed

        student.save()

        return redirect('/viewstudent')
    else:
        return HttpResponse("Failed")

    return render(request, 'update.html', {'student': student})


# Login Page
def login(request):
    return render(request, 'login.html')


# Login Check
# def logincheck(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         student = reg.objects.filter(
#             email=email,
#             password=password
#         ).first()

#         if student:
#             request.session['student_id'] = student.id       #Session started 
#             # return HttpResponse("Login Successfully!")
#             return redirect('dashboard')
#         else:
#             # return HttpResponse("Login Failed!")
#                 return redirect('login')
    
#     return render(request, 'login.html')



def logincheck(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        student = reg.objects.filter(
            email=email,
            password=password
        ).first()

        if student:
            request.session['student_id'] = student.id
            messages.success(request, "Login Successfully!")
            return redirect('dashboard')

        else:
            messages.error(request, "Login Failed!")
            return redirect('login')

    return render(request, 'login.html')


#Dashboard
# def dashboard(request):
#     if request.session.get('student_id'):
#         student = reg.objects.get(id=request.session.get('student_id'))
    
#     data=student.objects.filter(email=student.email).first()
    
#     return render(request, 'dashboard.html', {'data': data})
# else:
#     return redirect("login")
    
    return render(request, 'dashboard.html')
    
# def dashboard(request):
#     if request.session.get('student_id'):
#         student = reg.objects.get(
#             id=request.session.get('student_id')
#         )

#         return render(request, 'dashboard.html', {'data': student})

#     return redirect('login')

# def dashboard(request):
#     if request.session.get('student_id'):
#         student = reg.objects.get(
#             id=request.session.get('student_id')
#         )
#         messages.success(request, "Login Successfully!")
#         return render(request, 'dashboard.html', {'data': student})
#     else:
#         messages.warning(request,"Login Failed!")
#     return redirect('login')

def dashboard(request):
    if request.session.get('student_id'):
        student = reg.objects.get(
            id=request.session.get('student_id')
        )

       # messages.success(request, "Login Successfully!")

        return render(
            request,
            'dashboard.html',
            {'data': student}
        )

    messages.warning(request, "Please Login First!")
    return redirect('login')

# Logout
def user_logout(request):
    logout(request)
    del request.session['student_id']  # Session Ended
    return redirect('login')

def add_cookie(request):
    res=HttpResponse("Cookies Set")
    res.set_cookie('name', 'Ganesh Mahajan')
    return res

def view_cookie(request):
    name=request.COOKIES.get('name')
    return HttpResponse("Name: "+name)


def file(request):
    return render(request, 'file.html')

# def file_upload(request):
#     if request.method == "POST":
#         email=request.POST['email']
#         photo=request.FILES['photo']

#         emp=reg.employee(email=email, photo=photo)
#         emp.save()

#         return HttpResponse("File Uploaded Successfully!")
#     else:
#          #return HttpResponse("Failed")
    
#      return render(request, 'file.html')


def file_upload(request):
    if request.method == "POST":
        email = request.POST.get('email')
        photo = request.FILES.get('photo')

        emp = employee(
            email=email,
            photo=photo
        )

        emp.save()
        messages.success(request, "File Uploded Successfully!")
        
        #return redirect('file')
        
    else:
        messages.warning(request, "File Upload Failed!")
        return messages.warning
        #return redirect('/')


        return render(request, 'file.html', {
            'msg': 'File Uploaded Successfully'
        })

    return render(request, 'file.html')


def form(request):
    p = PersonForm()
    return render(request, 'form.html', {'p': p})

from .forms import PersonForm

def form(request):
    p=PersonForm()
    return render(request, 'form.html', {'form': p})
        


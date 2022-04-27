from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student, Track
from .forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# # Create your views here.


# def signupPg(requestp):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         signup_form = UserForm()
#         if(request.method =='POST'):
#             signup_form = UserForm(request.POST)
#             if(signup_form.is_valid()):
#                 signup_form.save()
#                 msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
#                 messages.info(request, msg)
#                 return redirect ('login')
#         context = {' signup_form': signup_form}
#         return render( request, 'tunapp/signup.html', context)



@api_view(['GET'])
def api_all_student(request):
    all_st = Student.objects.all()
    st_ser = StudentSerializer(all_st, many = True)
    return Response(st_ser.data)


@api_view(['GET'])
def api_one_student(request , st_id):
    st= Student.objects.get(id = st_id)
    st_ser = StudentSerializer(st, many = False)
    return Response(st_ser.data)  

@api_view(['POST'])
def api_add_student(request):
    st_ser = StudentSerializer(data=request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')   

@api_view(['POST'])
def api_edit_student(request , st_id):
    st= Student.objects.get(id = st_id)
    st_ser = StudentSerializer(data=request.data , instance=st)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all') 

@api_view(['DELETE'])
def api_del_student(request, st_id):
     st= Student.objects.get(id = st_id)
     st.delete()
     return Response('student deleted')


def home(request):
    all_students = Student.objects.all()
    return render(request, 'djapp/home.html', {'student_list':all_students})

def show(request , st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st }
    return render(request,'djapp/show.html',context)


def del_st(request , st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return redirect('home')


def addstudent(request):
    st_form = StudentForm()
    if request.method == 'POST':
         st_form = StudentForm(request.POST)
         if st_form.is_valid():
             st_form.save()
             return redirect('home')
    context = {'st_form' : st_form }
    return render(request, 'djapp/add.html' , context)


def editStudent(request , st_id):
    st = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=st)
    if request.method == 'POST':
        st_form = StudentForm(request.POST, instance=st)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'st_form' : st_form }
    return render(request, 'djapp/add.html' , context)
    
       
       


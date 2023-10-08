from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from .models import Student, Course, Cart, OrderPlaced
from .forms import StudentRegistration
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#def home(request):
 #   return render(request, 'home/home.html')

class CourseView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'home/home.html', {'courses':courses})

class CourseDetailView(View):
  def get(self,request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'home/coursedetail.html',{'course': course})

@login_required
def add_to_list(request):
 user = request.user
 course_id = request.GET.get('course_id')
 course = Course.objects.get(id=course_id)
 Cart(user=user, course=course).save()
 return redirect('/list')

@login_required
def show_list(request):
    if request.user.is_authenticated:
        user = request.user
        amount=0.0
        total_amount = 0.0
        list_course=[c for c in Cart.objects.all() if c.user==user]
        if list_course:
            for c in list_course:
                tempamount = c.course.discounted_price
                amount += tempamount
                totalamount = amount
            list_course = Cart.objects.filter(user=user)
            return render(request, 'home/addtolist.html',{'list_course':list_course, 'amount':amount, 'totalamount':totalamount})
        else:
            return render(request, 'home/emptylist.html')

#Remove Item
def remove_item(request):
    if request.method == 'GET':
        course_id = request.GET['course_id']
        p = Cart.objects.get(Q(course=course_id) & Q(user=requset.user))
        p.delete()
        amount = 0.0
        list_course = [ c for c in Cart.objects.all() if c.user == request.user]
        for c in list_course:
            tempamount = c.course.dicounted_price
            amount += tempamount
        data={
            'amount' : amount,
            'totalamount' : amount
        }
        
        return JsonResponse(data)

 

def enrol_now(request):
 return render(request, 'home/enrolnow.html')

def about(request):
    return render(request, 'home/about.html')

def success(request):
    return render(request, 'home/submit.html')

#def registration(request):
 #   return render(request, 'home/registration.html')


class StudentRegistrationView(View):
        def get(self,request):
            form = StudentRegistration()
            return render(request, 'home/registration.html', {'form':form})

        def post(self,request):
            form = StudentRegistration(request.POST)
            if form.is_valid():
                messages.success(request, "Registration Completed")
                form.save()
            return render(request, 'home/registration.html', {'form':form})

def profile(request):
 return render(request, 'home/profile.html')

def contact(request):
    return render(request, 'home/contact.html')

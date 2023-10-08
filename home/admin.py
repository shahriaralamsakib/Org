from django.contrib import admin
from .models import (
    Student,
    Course,
    Cart,
    OrderPlaced
)

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','email')

admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title','selling_price','discounted_price','description','category','course_image')

admin.site.register(Course,CourseAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','course']

admin.site.register(Cart,CartAdmin)

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'student','course','ordered_date','status']

admin.site.register(OrderPlaced,OrderPlacedAdmin)
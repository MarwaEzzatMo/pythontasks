from dataclasses import fields
from django.contrib import admin
from .models import Student ,Track
# Register your models here.


class CustomStudent(admin.ModelAdmin):
    fieldsetd = (
        ['dtudent informtion', {'fields':{'fname','lname','age'}}],
        ['Scholarship info ', {'fields':{'student_track'}}]
    )
    list_display = ('fname','lname','age','student_track','is_adult')
    search_fields = ('fname','lname','age','student_track__track_name')
    list_filter = ('age','student_track__track_name')

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 3

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]    


admin.site.register(Student,CustomStudent)
admin.site.register(Track,CustomTrack)

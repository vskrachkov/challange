from django.contrib import admin
from students.models import Group, Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

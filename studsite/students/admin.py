from django.contrib import admin
from students.models import Group, Student


class StudentInline(admin.TabularInline):
    model = Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions_on_top = False
    actions_on_bottom = True
    empty_value_display = '???'
    list_display = ('full_name', 'group')
    fieldsets = (
        (
            u'ФИО',
            {
                'fields': ('first_name', 'second_name', 'last_name'),
                'classes': ('collapse',),
                'description': u'Имя, фамилия и отчество студента'
            }
        ),
        (
            u'Дополнительно',
            {
                'fields': ('student_ID', 'group'),
            }
        ),
        (
            None,
            {
                'fields': ('starosta',),
            }
        ),
    )

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from students.models import Group, Student


class GroupListView(ListView):
    model = Group
    template_name = "students/groups.html"
    context_object_name = 'group_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = u'Список групп'
        return context


class GroupDetailView(DetailView):
    model = Group
    template_name = "students/group_detail.html"
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = u'Группа {0}'.format(
            Group.objects.get(pk=int(self.kwargs['pk'])).name)

        self.request.session['group_pk'] = self.kwargs['pk']
        return context


class GroupUpdateView(UpdateView):
    model = Group
    template_name = "students/update.html"
    fields = ('name', )


class GroupCreateView(CreateView):
    model = Group
    template_name = "students/create.html"
    fields = ('name', )


class GroupDeleteView(DeleteView):
    model = Group
    template_name = "students/delete.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "students/create.html"
    fields = (
        'first_name',
        'second_name',
        'last_name',
        'student_ID',
        'group',
        'starosta',
    )

    def get_initial(self):
        group_pk = self.request.session['group_pk']
        return {
            'group': Group.objects.get(pk=group_pk)
        }


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/delete.html"

    def get_success_url(self, **kwargs):
        if kwargs.get('pk'):
            return reverse('group_detail', **{'pk': kwargs.get('pk')})
        else:
            return reverse('groups')


class StudentUpdateView(StudentCreateView, UpdateView):
    template_name = "students/update.html"

from django.shortcuts import render
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
        return context


class GroupUpdateView(UpdateView):
    model = Group
    template_name = "students/group_update.html"
    fields = ('name', )


class GroupCreateView(CreateView):
    model = Group
    template_name = "students/group_create.html"
    fields = ('name', )


class GroupDeleteView(DeleteView):
    model = Group
    template_name = "students/group_delete.html"
    fields = ('name', )

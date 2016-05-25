from django.conf.urls import url


from students.views import GroupListView, GroupDetailView, GroupUpdateView, \
    GroupCreateView, GroupDeleteView, StudentCreateView, StudentDeleteView, \
    StudentUpdateView


urlpatterns = [
    url(r'^groups$', GroupListView.as_view(), name='groups'),

    url(r'^group/(?P<pk>[0-9]+)/$',
        GroupDetailView.as_view(), name='group_detail'),

    url(r'^group/(?P<pk>[0-9]+)/update',
        GroupUpdateView.as_view(success_url='/groups'), name='group_update'),
    url(r'^group/create$',
        GroupCreateView.as_view(success_url='/groups'), name='group_create'),
    url(r'^group/(?P<pk>[0-9]+)/delate',
        GroupDeleteView.as_view(success_url='/groups'), name='group_delete'),

    url(r'^student/create$',
        StudentCreateView.as_view(success_url='/groups'), name='student_create'),
    url(r'^student/(?P<pk>[0-9]+)/delate',
        StudentDeleteView.as_view(success_url='/groups'), name='student_delete'),
    url(r'^student/(?P<pk>[0-9]+)/update',
        StudentUpdateView.as_view(success_url='/groups'), name='student_update'),
    

]

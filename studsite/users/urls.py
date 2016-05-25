from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(
        r'/login',
        auth_views.login,
        {
            'template_name': 'users/login.html',
        },
        name='login'
    ),
    url(
        '',
        auth_views.logout_then_login,
        {'login_url': 'login'},
        name='logout',
    ),
    url(
        r'password_change',
        auth_views.password_change,
        {
            'template_name': 'users/password_change.html',
            'post_change_redirected': 'groups',
        },
        name='password_change'
    ),

]

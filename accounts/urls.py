from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns=[
    path('succees/',TemplateView.as_view(template_name='accounts/succees.html'),name='password_succees'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('role/',views.role_change ,name='role_change'),
    path('forget/',views.forget_password_post ,name='forget_password'),
    path('done/password/',views.done_password_post ,name='done_password'),

]
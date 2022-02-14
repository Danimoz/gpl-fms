"""dms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from dept.admin import dept_site
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
    path('pwd-change-done/', 
        auth_views.PasswordChangeDoneView.as_view(template_name='pages/password_change_done.html'), 
        name='pwdchange_done'),
    path('pwd-reset/', 
        auth_views.PasswordResetView.as_view(template_name='pages/password_reset.html'), 
        name='password_reset'),
    path('pwd-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'), 
        name='password_reset_done'),
    path('pwd-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='pages/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('pwd-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='pages/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('pwd-change/', 
        auth_views.PasswordChangeView.as_view(
            template_name='pages/password_change_form.html',
            success_url = '/pwd-change-done'
            ), 
        name='pwdchange'),
    path('sadmin/', dept_site.urls, name="sadmin"),
    path('', include('dept.urls'), name="home"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.conf.urls.static import static

urlpatterns = [

    path('',views.CourseView.as_view(), name='home'),
    path('course-detail/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('list/', views.show_list, name='showlist'),
    path('removeitem/', views.remove_item),
    path('enrol/', views.enrol_now, name='enrol-now'),
    path('about/',views.about, name='about'),
    path('registration/',views.StudentRegistrationView.as_view(), name='reg'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='home/login.html', authentication_form=LoginForm), name='login'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='home/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name = 'passwordchange'),
    
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name = 'home/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='home/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'), name='password_reset_complete'),



    path('profile/', views.profile, name='profile'),
    path('contact/',views.contact, name='con'),
    path('successfully/',views.success, name = 'successfully'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
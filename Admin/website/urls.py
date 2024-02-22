from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    path("blocked/", views.home, name="blocked"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
    path("edit_record/<int:pk>", views.edit_record, name="edit_record"),
    # path("business_record/", views.B_record, name="B_record"),
    path("upload/", views.upload, name="upload"),
    path("monitor/", views.traffic_monitor, name="monitor"),
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="password_reset"),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),  

]

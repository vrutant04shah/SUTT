from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("login/", views.login, name="login"),
        path("profile/", views.profile, name="profile"),
        path("staff/register/", views.staff_register, name="staff-register"),
        path("staff/login/", auth_views.LoginView.as_view(template_name='home/login.html'), name="staff-login"),
        path("staff/logout/", auth_views.LogoutView.as_view(template_name='home/logout.html'), name="staff-logout"),
        path("new/doctor/", views.new_doctor, name="new-doctor"),
        path('apply/appointment/', views.appointment, name="apply-appointment"),
        path('billing/', views.billing, name='billing'),
        path('approval/', views.approval, name='approval'),
        path('reject/<int:appointment_id>/', views.appointment_reject, name='reject-approval'),
        path('approve/<int:appointment_id>/', views.appointment_approve, name='approve-approval'),
        path('approved/appointment/', views.approved_appointment, name='approved-appointment'),
        path('search/results/', views.search_result, name='search-result'),
        path('search/profile/<int:user_id>', views.search_profile, name='search-profile'),
        path('patients/table/', views.patient_table, name='patient-table'),
        path('doctor/table/', views.doctor_table, name='doctor-table'),
        path('new/bills/', views.create_bills, name='new-bills'),
    ]

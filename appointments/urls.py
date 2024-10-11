from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    dashboard_view,
    # create_appointment_view,
    view_appointments,
    manage_availability_view,
    book_appointment,
    home_view,
    # view_appointment_detail,
    confirm_appointment,
    cancel_appointment,
    delete_appointment,
    delete_availability,
)



urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    # path('create_appointment/', create_appointment_view, name='create_appointment'),
    path('view/', view_appointments, name='view_appointments'),
    path('confirm/<int:appointment_id>/', confirm_appointment, name='confirm_appointment'),
    path('cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    # path('<int:id>/detail/',view_appointment_detail, name='view_appointment_detail'),
    path('manage_appointments/', manage_availability_view, name='manage_availability_view'),
    path('book_appointment/', book_appointment, name='book_appointment'),
   path('delete_availability/<int:availability_id>/', delete_availability, name='delete_availability'),
]

from .registration import register_view
from .authentication import login_view, logout_view
from .appointments import (
    # create_appointment_view,
    view_appointments,
    manage_availability_view,
    book_appointment,
    dashboard_view,
    home_view,
    # view_appointment_detail,
    confirm_appointment,
    cancel_appointment,
    delete_appointment,
    delete_availability,
)

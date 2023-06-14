from django.contrib import admin
from .models import User, Doctor, Appointment, Billing, Approved_Appointment

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Billing)
admin.site.register(Approved_Appointment)

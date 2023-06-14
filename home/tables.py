import django_tables2 as tables
from users.models import User, Doctor


class PatientTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", "age", "gender")


class DoctorTable(tables.Table):
    class Meta:
        model = Doctor
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "age", "doctor")

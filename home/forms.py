from django import forms
from users.models import User, Doctor, Appointment, Approved_Appointment, Billing
from django.contrib.auth.forms import UserCreationForm


class Staff_RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'gender', 'password1', 'password2']


class ProfileUpdationForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'gender']


class PatientProfileUpdationForm(forms.ModelForm):
    age = forms.IntegerField()
    gender = forms.CharField(max_length=100)
    illness_history = forms.Textarea()

    class Meta:
        model = User
        fields = ['username', 'age', 'gender', 'illness_history']


class Staff_PatientUpdationForm(forms.ModelForm):
    illness_history = forms.Textarea()
    prescriptions = forms.Textarea()

    class Meta:
        model = User
        fields = ['illness_history', 'prescriptions']


class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'age', 'doctor']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['description', 'doc_type', 'complaints']


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approved_Appointment
        fields = ['doctor', 'appointment']


class BillingForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    user = forms.ModelChoiceField(queryset=User.objects.all().filter(is_staff=False), empty_label=None)
    date = forms.DateField()

    class Meta:
        model = Billing
        fields = ['user', 'amount', 'date']


class ChatForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False), empty_label=None)

    class Meta:
        model = User
        fields = ['user']

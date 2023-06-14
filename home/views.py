import fuzzywuzzy.fuzz
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Staff_RegistrationForm, ProfileUpdationForm, DoctorCreationForm, AppointmentForm, ApprovalForm, PatientProfileUpdationForm, Staff_PatientUpdationForm, BillingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Billing, Appointment, Approved_Appointment, User, Doctor
from fuzzywuzzy import process
from .tables import PatientTable, DoctorTable


def home(request):
    return render(request, 'home/home.html')


def login(request):
    return render(request, 'home/login_page.html')


def staff_register(request):
    if request.method == "POST":
        form = Staff_RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.age = form.cleaned_data.get('age')
            user.gender = form.cleaned_data.get('gender')
            user.illness_history = 'None'
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!! You can login now.')
            return redirect('login')
    else:
        form = Staff_RegistrationForm()
    return render(request, 'home/register.html', {'form': form})


@login_required    
def profile(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = ProfileUpdationForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account updated!')
                return redirect('profile')
        else:
            form = ProfileUpdationForm(instance=request.user)
        return render(request, 'home/profile.html', {'form': form})
    else:
        return patient_profile(request)


def patient_profile(request):
    if request.method == "POST":
        form = PatientProfileUpdationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated!')
            return redirect('profile')
    else:
        form = PatientProfileUpdationForm(instance=request.user)
    return render(request, 'home/profile.html', {'form': form})


def new_doctor(request):
    if request.method == "POST":
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request, f'{username} added to the system!!')
            return redirect('new-doctor')
    else:
        form = DoctorCreationForm()
    return render(request, 'home/doctor.html', {'form': form})


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Applied for Appointment !! Please wait for Approval!')
            return redirect('apply-appointment')
    else:
        form = AppointmentForm()
    return render(request, 'home/appointment.html', {'form': form})


def billing(request):
    user = request.user
    bills = Billing.objects.all().filter(user=user)
    remaining_bills = Billing.objects.all().filter(user=user, status=False)
    total_amount = sum(bill.amount for bill in bills)
    remaining_amount = sum(remaining_bill.amount for remaining_bill in remaining_bills)
    context = {
        'bills': bills,
        'remaining_amount': remaining_amount,
        'total_amount': total_amount,
        }
    return render(request, 'home/billing.html', context)


def approval(request):
    context = {
        'appointments': Appointment.objects.all().filter(approval=False)
        }
    return render(request, 'home/approval.html', context)


def appointment_reject(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        appointment.delete()
        return redirect('approval')
    return render(request, 'home/appointment_reject.html')


def appointment_approve(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            approve = form.save(commit=False)
            if approve.doctor.doctor == appointment.doc_type:
                appointment.approval = True
                doctor = approve.doctor
                appointment.save()
                approve.save()
                return redirect('approval')
    else:
        form = ApprovalForm()
    return render(request, 'home/appointment_approve.html', {'form': form})


def approved_appointment(request):
    user = request.user
    appointments = Approved_Appointment.objects.all()
    approved = []
    for appointment in appointments:
        if appointment.appointment.approval == True and appointment.appointment.user == user:
            approved.append(appointment)
    
    context = {
        'approved': approved
        }
    return render(request, 'home/approved_appointment.html', context)


def search_result(request):
    query = request.GET.get('query')
    patients = User.objects.all().filter(is_staff=False)
    search_results_list = []
    if query:
        search_results = process.extract(query, patients, scorer=fuzzywuzzy.fuzz.token_sort_ratio, limit=10)
        # search_results_list = [search_result[0] for search_result in search_results]
    for search_result in search_results:
        search_results_list.append(search_result[0])

    context = {
        'query': query,
        'search_results': search_results_list,
    }
    return render(request, 'home/result.html', context)


def search_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = Staff_PatientUpdationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search-profile')
    else:
        form = Staff_PatientUpdationForm()
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'home/search_profile.html', context)


def patient_table(request):
    queryset = User.objects.filter(is_staff=False)
    table = PatientTable(queryset)
    return render(request, 'home/patient_table.html', {'table': table})


def doctor_table(request):
    queryset = Doctor.objects.all()
    table = DoctorTable(queryset)
    return render(request, 'home/doctor_table.html', {'table': table})


def create_bills(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BillingForm()
    return render(request, 'home/create_bills.html', {'form': form})


from django.shortcuts import render


def home(request):
    return render(request, 'patient_info/index.html')
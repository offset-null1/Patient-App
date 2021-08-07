from django.shortcuts import render
from .forms import Register
from .models import Patient
from django.contrib import messages
def home(request):
    
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            option = form.cleaned_data['option']
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            disease = form.cleaned_data['disease']
            doctor_name = form.cleaned_data['doctorName']
            fees = form.cleaned_data['fees']
            started_med_on_date = form.cleaned_data['started_med_on_date']   
            
            print(first_name,started_med_on_date)   
            
            if(option == '0'): 
                p = Patient(first_name=first_name, last_name=last_name, gender=gender, age=age, disease=disease, doctor_name=doctor_name, fees=fees, started_med_on_date=started_med_on_date)
                p.save()   
            
            elif(option == '1'):
                if Patient.objects.filter(first_name=first_name).exists() and Patient.objects.filter(last_name=last_name).exists():
                    p = Patient(first_name=first_name, last_name=last_name, gender=gender, age=age, disease=disease, doctor_name=doctor_name, fees=fees, started_med_on_date=started_med_on_date)
                    p.save()  
                    messages.success(request, "You successfully updated the Patient record")
 
   
            else: 
                p = Patient.objects.get(first_name=first_name, last_name=last_name, gender=gender, age=age, disease=disease, doctor_name=doctor_name, fees=fees, started_med_on_date=started_med_on_date)
                p.delete()
    
    form = Register()
    return render(request, 'patient_info/index.html', {'form': form})

from django import forms

# GENDER = (
#     ('0', 'Male', 'male'),
#     ('1', 'Female', 'female'),
#     ('2', 'Others', 'others')
# )

class DateInput(forms.DateInput):
    input_type = 'date'

class Register(forms.Form):
    option = forms.ChoiceField(choices=[('0','Create'),('1','Update'),('2','Delete')],required=True, label='Option: ')
    fname = forms.CharField(max_length=50,required=True,label='First Name: ')
    lname = forms.CharField(max_length=50,required=True, label='Last Name: ')
    gender = forms.ChoiceField(choices=[('0','Male'),('1','Female'),('2','Others')], label='Gender: ')
    age = forms.IntegerField(label='Age: ')
    disease = forms.CharField(max_length=70,label='Disease: ')
    doctorName = forms.CharField(max_length=100,label="Doctor's Name: ")
    fees = forms.DecimalField(label='Fees: ')
    started_med_on_date = forms.DateField(label="Enter the date when your treatment started: ",widget=DateInput())
    
    

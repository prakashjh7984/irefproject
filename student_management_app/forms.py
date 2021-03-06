from cProfile import label
from faulthandler import disable
from locale import currency
from django import forms
from django.forms import ModelForm, PasswordInput, widgets
from django.forms import ChoiceField
from student_management_app import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from student_management_app.models import Country, Courses, Semesters, SessionYearModel, Staffs, State, Subjects, Students,Notice




class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass


class DateInput(forms.DateInput):
    input_type = "date"

class NumberInput(forms.NumberInput):
    input_type = "number"

class AddStudentForm(forms.Form): 
    def __init__(self,list_courses,session_list,country_list,State_list,*args,**kwargs):
        super(AddStudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].choices = list_courses
        self.fields['session_year'].choices = session_list

        self.fields['country'].choices = country_list
        self.fields['state'].choices = State_list
        
        # breakpoint()
        # if 'country' in self.fields:
        #     try:
        #         country_id = int(self.fields.get('country'))
        #         self.fields['state'].queryset = State.objects.filter(country=country_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # # elif self.instance.id:
        # #     self.fields['state'].queryset = self.instance.country.State_set.order_by('name')
        # else:
        #     self.fields['state'].queryset = State.objects.all().order_by('name')
       
    

        
        
    
    
    
    email=forms.EmailField(label="Email (*must required)",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control","autocomplete":"off"}))
    # prn_number=forms.CharField(label="PRN(Permanent Registration Number)[optional]",required=False,max_length=20,widget=forms.NumberInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password (*Must required)",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control","data-toggle": "password"}))
    
    first_name=forms.CharField(label="First Name *(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name *(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username *(required)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    profile_pic=forms.FileField(label="Profile Pic *(Photo > Small Passport size photo)",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))



    
    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )

    currency_choice=(
        ("INR","INR"),
        ("USD","USD"),
       
    )

    admission_choice=(
        ("Full Time","Full Time"),
        ("Part Time","Part Time"),
        ("Distance","Distance"),
        ("Online","Online"),
        ("Diploma","Diploma"),
        ("Certification","Certification")
    )

    status_choice=(
        ("Provisional","Provisional"),
        ("Confirmed","Confirmed"),
        ("Others","Others")

    )

    session_choice=(
        ("Jan","Jan"),
        ("Feb","Feb"),
        ("Mar","Mar"),
        ("Apr","Apr"),
        ("May","May"),
        ("Jun","Jun"),
        ("Jul","Jul"),
        ("Aug","Aug"),
        ("Sep","Sep"),
        ("Oct","Oct"),
        ("Nov","Nov"),
        ("Dec","Dec")
    )

    qualification_choice=(
        ("10","10"),
        ("10+2","10+2"),
        ("Diploma","Diploma"),
        ("Graduation","Graduation"),
        ("Post Graduation","Post Graduation"),
        ("Others","Others")
    )

    work_choice=(
        ("Select","Select"),
        ("Fresher","Fresher"),
        ("1-2","1-2"),
        ("3-6","3-6"),
        ("6-10","6-10"),
        ("10+","10+"),
    )

    course=forms.ChoiceField(label="Course *",widget=forms.Select(attrs={"class":"form-control"}))
    
    gender=forms.ChoiceField(label="Gender *",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    father_name=forms.CharField(label="Father name *",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    mother_name=forms.CharField(label="Mother name *",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_of_birth=forms.DateField(label="Date of birth *",widget=DateInput(attrs={"class":"form-control"}))
    admission_type=forms.ChoiceField(label="Admission type(optional)",choices=admission_choice,widget=forms.Select(attrs={"class":"form-control"}))
    admission_status=forms.ChoiceField(label="admission status *",choices=status_choice,widget=forms.Select(attrs={"class":"form-control"}))

    country=forms.ChoiceField(label="Country *(Select country to see states)",widget=forms.Select(attrs={"class":"form-control"}))
    state=forms.ChoiceField(label="State *",widget=forms.Select(attrs={"class":"form-control"}))

    permanent_address=forms.CharField(label="permanent address *",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    communication_address=forms.CharField(label="communication address *",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    session_year=forms.ChoiceField(label="Session Year *",widget=forms.Select(attrs={"class":"form-control"}))
    session_joining_month=forms.ChoiceField(label="Session Joining Month *",choices=session_choice,widget=forms.Select(attrs={"class":"form-control"}))
    mobile=forms.CharField(label="mobile *",max_length=20,widget=forms.NumberInput(attrs={"class":"form-control"}))
    alternate_mobile=forms.CharField(label="alternate mobile *",max_length=20,widget=forms.NumberInput(attrs={"class":"form-control"}))
    highest_qualification=forms.ChoiceField(label="Highest qualification *",choices=qualification_choice,widget=forms.Select(attrs={"class":"form-control"}))
    work_experience=forms.ChoiceField(label="Total work experience *",choices=work_choice,widget=forms.Select(attrs={"class":"form-control"}))
    currency_type=forms.ChoiceField(label="Currency type *",choices=currency_choice,widget=forms.Select(attrs={"class":"form-control"}))
    final_fees=forms.CharField(label="Final fees *",max_length=50,widget=forms.NumberInput(attrs={"class":"form-control"}))
    other_information=forms.CharField(label="Other information *",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))

class ChangePasswordForm(forms.Form):
       password=forms.CharField(label="Password (*Type strong password)",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter only when you have to change password"}))

class EditStudentForm(forms.Form):
    # breakpoint()
    def __init__(self,list_courses,list_exam_courses,session_list,country_list,state_list,*args,**kwargs):
        super(EditStudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].choices = list_courses
        self.fields['exam_course'].choices = list_exam_courses
        self.fields['session_year'].choices = session_list
        self.fields['country'].choices = country_list
        self.fields['state'].choices = state_list

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    # password=forms.CharField(label="Password (*Must required)",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    prn_number=forms.CharField(required=False,label="PRN(Permanent Registration Number)",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    exam_course=forms.ChoiceField(label="Exam Course",widget=forms.Select(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required = False,label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic (Photo > Small Passport size photo)",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


    # course_list=[]
    # try:
    #     courses = Courses.objects.all()
    #     for course in courses:
    #         small_course=(course.id,course.course_name)
    #         course_list.append(small_course)
    # except:
    #     course_list=[]

    # session_list = []
    # try:
    #     sessions = SessionYearModel.object.all()

    #     for ses in sessions:
    #         small_ses = (ses.id, str(ses.session_start_year)+"   TO  "+str(ses.session_end_year))
    #         session_list.append(small_ses)
    # except:
    #     session_list = []

    # countries=[]
    # try:
    #     country_list = Country.objects.all()

    #     for country in country_list:
    #         country_name=(country.id,country.name)
    #         countries.append(country_name)
            
    # except:
    #     countries=[]

    # state_list=[]
    # try:
    #     states = State.objects.all()
    #     for state in states:
    #         state_name=(state.id,state.name)
    #         state_list.append(state_name)
    # except:
    #     state_list=[]

    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )

    currency_choice=(
        ("INR","INR"),
        ("USD","USD"),
       
    )

    admission_choice=(
        ("Full Time","Full Time"),
        ("Part Time","Part Time"),
        ("Distance","Distance"),
        ("Online","Online"),
        ("Diploma","Diploma"),
        ("Certification","Certification")
    )

    status_choice=(
        ("Provisional","Provisional"),
        ("Confirmed","Confirmed"),
        ("Others","Others")

    )

    session_choice=(
        ("Jan","Jan"),
        ("Feb","Feb"),
        ("Mar","Mar"),
        ("Apr","Apr"),
        ("May","May"),
        ("Jun","Jun"),
        ("Jul","Jul"),
        ("Aug","Aug"),
        ("Sep","Sep"),
        ("Oct","Oct"),
        ("Nov","Nov"),
        ("Dec","Dec")
    )

    qualification_choice=(
        ("10","10"),
        ("10+2","10+2"),
        ("Diploma","Diploma"),
        ("Graduation","Graduation"),
        ("Post Graduation","Post Graduation"),
        ("Others","Others")
    )

    work_choice=(
        ("Fresher","Fresher"),
        ("1-2","1-2"),
        ("3-6","3-6"),
        ("6-10","6-10"),
        ("10+","10+"),
    )

    course=forms.ChoiceField(label="Course",widget=forms.Select(attrs={"class":"form-control"}))
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    father_name=forms.CharField(label="Father name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    mother_name=forms.CharField(label="Mother name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_of_birth=forms.DateField(label="date_of_birth",widget=DateInput(attrs={"class":"form-control"}))
    admission_type=forms.ChoiceField(label="Admission type",choices=admission_choice,widget=forms.Select(attrs={"class":"form-control"}))
    admission_status=forms.ChoiceField(label="admission status",choices=status_choice,widget=forms.Select(attrs={"class":"form-control"}))

    country=forms.ChoiceField(label="Country",widget=forms.Select(attrs={"class":"form-control"}))
    state=forms.ChoiceField(label="State",widget=forms.Select(attrs={"class":"form-control"}))

    permanent_address=forms.CharField(label="permanent address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    communication_address=forms.CharField(label="communication address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    session_year=forms.ChoiceField(label="Session Year",widget=forms.Select(attrs={"class":"form-control"}))
    session_joining_month=forms.ChoiceField(label="Session Joining Month",choices=session_choice,widget=forms.Select(attrs={"class":"form-control"}))
    mobile=forms.CharField(label="mobile",max_length=50,widget=forms.NumberInput(attrs={"class":"form-control"}))
    alternate_mobile=forms.CharField(label="alternate mobile",max_length=20,widget=forms.NumberInput(attrs={"class":"form-control"}))
    highest_qualification=forms.ChoiceField(label="Highest qualification",choices=qualification_choice,widget=forms.Select(attrs={"class":"form-control"}))
    work_experience=forms.ChoiceField(label="Total work experience",choices=work_choice,widget=forms.Select(attrs={"class":"form-control"}))
    currency_type=forms.ChoiceField(label="Currency type",choices=currency_choice,widget=forms.Select(attrs={"class":"form-control"}))
    final_fees=forms.CharField(label="Final fees",max_length=50,widget=forms.NumberInput(attrs={"class":"form-control"}))
    other_information=forms.CharField(label="Other information",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))


class EditStudentProfile(forms.Form):
    # breakpoint()
    def __init__(self,list_courses,session_list,country_list,state_list,*args,**kwargs):
        super(EditStudentProfile,self).__init__(*args,**kwargs)
        self.fields['course'].choices = list_courses
        self.fields['session_year'].choices = session_list
        self.fields['country'].choices = country_list
        self.fields['state'].choices = state_list
        # self.fields['email']['readonly'] = True

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control",'readonly': True}))
    prn_number=forms.CharField(required=False,label="PRN(Permanent Registration Number)",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name(put the name as on  the previous marksheet)",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required = False,label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic (Photo > Small Passport size photo)",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


    # course_list=[]
    # try:
    #     courses = Courses.objects.all()
    #     for course in courses:
    #         small_course=(course.id,course.course_name)
    #         course_list.append(small_course)
    # except:
    #     course_list=[]

    # session_list = []
    # try:
    #     sessions = SessionYearModel.object.all()

    #     for ses in sessions:
    #         small_ses = (ses.id, str(ses.session_start_year)+"   TO  "+str(ses.session_end_year))
    #         session_list.append(small_ses)
    # except:
    #     session_list = []

    # countries=[]
    # try:
    #     country_list = Country.objects.all()

    #     for country in country_list:
    #         country_name=(country.id,country.name)
    #         countries.append(country_name)
            
    # except:
    #     countries=[]

    

    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )

    currency_choice=(
        ("INR","INR"),
        ("USD","USD"),
       
    )

    admission_choice=(
        ("Full Time","Full Time"),
        ("Part Time","Part Time"),
        ("Distance","Distance"),
        ("Online","Online"),
        ("Diploma","Diploma"),
        ("Certification","Certification")
    )

    status_choice=(
        ("Provisional","Provisional"),
        ("Confirmed","Confirmed"),
        ("Others","Others")

    )

    session_choice=(
        ("Jan","Jan"),
        ("Feb","Feb"),
        ("Mar","Mar"),
        ("Apr","Apr"),
        ("May","May"),
        ("Jun","Jun"),
        ("Jul","Jul"),
        ("Aug","Aug"),
        ("Sep","Sep"),
        ("Oct","Oct"),
        ("Nov","Nov"),
        ("Dec","Dec")
    )

    qualification_choice=(
        ("10","10"),
        ("10+2","10+2"),
        ("Diploma","Diploma"),
        ("Graduation","Graduation"),
        ("Post Graduation","Post Graduation"),
        ("Others","Others")
    )

    work_choice=(
        ("Fresher","Fresher"),
        ("1-2","1-2"),
        ("3-6","3-6"),
        ("6-10","6-10"),
        ("10+","10+"),
    )

    course=forms.ChoiceField(label="Course",widget=forms.Select(attrs={"class":"form-control"}))
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    father_name=forms.CharField(label="Father name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    mother_name=forms.CharField(label="Mother name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_of_birth=forms.DateField(label="date_of_birth",widget=DateInput(attrs={"class":"form-control"}))
    admission_type=forms.ChoiceField(label="Admission type",choices=admission_choice,widget=forms.Select(attrs={"class":"form-control"}))
    admission_status=forms.ChoiceField(label="admission status",choices=status_choice,widget=forms.Select(attrs={"class":"form-control"}))

    country=forms.ChoiceField(label="Country",widget=forms.Select(attrs={"class":"form-control"}))
    state=forms.ChoiceField(label="State",widget=forms.Select(attrs={"class":"form-control"}))

    permanent_address=forms.CharField(label="permanent address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    communication_address=forms.CharField(label="communication address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    session_year=forms.ChoiceField(label="Session Year",widget=forms.Select(attrs={"class":"form-control"}))
    session_joining_month=forms.ChoiceField(label="Session Joining Month",choices=session_choice,widget=forms.Select(attrs={"class":"form-control"}))
    mobile=forms.CharField(label="mobile",max_length=50,widget=forms.NumberInput(attrs={"class":"form-control"}))
    alternate_mobile=forms.CharField(label="alternate mobile",max_length=20,widget=forms.NumberInput(attrs={"class":"form-control"}))
    highest_qualification=forms.ChoiceField(label="Highest qualification",choices=qualification_choice,widget=forms.Select(attrs={"class":"form-control"}))
    work_experience=forms.ChoiceField(label="Total work experience",choices=work_choice,widget=forms.Select(attrs={"class":"form-control"}))
    currency_type=forms.ChoiceField(label="Currency type",choices=currency_choice,widget=forms.Select(attrs={"class":"form-control"}))
    final_fees=forms.CharField(label="Final fees",max_length=50,widget=forms.NumberInput(attrs={"class":"form-control"}))
    other_information=forms.CharField(label="Other information",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    # password=forms.CharField(required = False,label="Change Password",max_length=255,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class AddCourseForm(forms.Form):
    def __init__(self,staff_list,course_list,*args,**kwargs):
        super(AddCourseForm,self).__init__(*args,**kwargs)
        self.fields['staff'].choices = staff_list
        self.fields['course_name'].choices = course_list
        # self.fields['course_code'].choices = code_list
        
    course_name=forms.CharField(label="Course",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    course_code=forms.CharField(label="Course Code",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    staff=forms.ChoiceField(label="Staff",widget=forms.Select(attrs={"class":"form-control"}))

class AddExamCourseForm(forms.Form):
    def __init__(self,course_list,*args,**kwargs):
        super(AddExamCourseForm,self).__init__(*args,**kwargs)
        # self.fields['staff'].choices = staff_list
        self.fields['course_name'].choices = course_list
        # self.fields['course_code'].choices = code_list
        
    course_name=forms.CharField(label="Course",max_length=100,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    course_code=forms.CharField(label="Course Code",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    # staff=forms.ChoiceField(label="Staff",widget=forms.Select(attrs={"class":"form-control"}))

class AddCountryForm(forms.Form):
      name= forms.CharField(label="Country",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))

class AddStudentOfferLetterForm(forms.Form):
    installment_date = forms.DateField(label="installment_date",widget=DateInput(attrs={"class":"form-control"}))
    fees = forms.CharField(label="fees",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    currency_type = (
    ("INR", "INR"),
    ("USD", "USD"),
    )
    currency_type = forms.ChoiceField(label="currency_type", choices=currency_type,widget=forms.Select(attrs={"class":"form-control"}))
    inr_fees = forms.CharField(label="fees in INR", widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    payment_status = (
        ("Fully Paid", "Fully Paid"),
        ("Partial Paid", "Partial Paid"),
        ("Unpaid", "Unpaid"),
    )
    payment_status=forms.ChoiceField(label="Payment Status",choices=payment_status,widget=forms.Select(attrs={"class":"form-control"}))
    note = forms.CharField(label="note",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))

class EditStudentOfferLetterForm(forms.Form):
    installment_date = forms.DateField(label="installment_date",widget=DateInput(attrs={"class":"form-control"}))
    fees = forms.CharField(label="fees",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    currency_type = (
    ("INR", "INR"),
    ("USD", "USD"),
    )
    currency_type = forms.ChoiceField(label="currency_type", choices=currency_type,widget=forms.Select(attrs={"class":"form-control"}))
    inr_fees = forms.CharField(label="fees in INR", widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    payment_status = (
        ("Fully Paid", "Fully Paid"),
        ("Partial Paid", "Partial Paid"),
        ("Unpaid", "Unpaid"),
    )
    payment_status=forms.ChoiceField(label="Payment Status",choices=payment_status,widget=forms.Select(attrs={"class":"form-control"}))
    note = forms.CharField(label="note",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))


class AddStudentPaymentReceiveForm(forms.Form):
    installment_date = forms.DateField(label="installment_date",widget=DateInput(attrs={"class":"form-control"}))
    installment_fees = forms.CharField(label="fees",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    currency_type = (
    ("INR", "INR"),
    ("USD", "USD"),
    )
    currency_type = forms.ChoiceField(label="currency_type", choices=currency_type,widget=forms.Select(attrs={"class":"form-control"}))
    inr_fees = forms.CharField(label="fees in INR", widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    invoice_no = forms.CharField(label="invoice_no",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    payment_options=(
        ("Cash","Cash"),
        ("Online Payment Gateway","Online Payment Gateway"),
         ("Bank Transfer","Bank Transfer"),
         ("Others", "Others"),
    )
    payment_status = (
        ("Fully Paid", "Fully Paid"),
        ("Partial Paid", "Partial Paid"),
        ("Unpaid", "Unpaid"),
    )
    payment_options=forms.ChoiceField(label="Payment options",choices=payment_options,widget=forms.Select(attrs={"class":"form-control"}))
    payment_status=forms.ChoiceField(label="Payment Status",choices=payment_status,widget=forms.Select(attrs={"class":"form-control"}))
    note = forms.CharField(label="note",widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))


class AddStateForm(forms.Form):
    def __init__(self,country_list,state_list,*args,**kwargs):
        super(AddStateForm,self).__init__(*args,**kwargs)
        self.fields['country'].choices = country_list
        self.fields['name'].choices = state_list
        

    country=forms.ChoiceField(label="Country(Select country to see states)",widget=forms.Select(attrs={"class":"form-control"}))
    name= forms.CharField(label="state",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    

class EditStateForm(forms.Form):
    def __init__(self,country_list,state_list,*args,**kwargs):
        super(EditStateForm,self).__init__(*args,**kwargs)
        self.fields['country'].choices = country_list
        self.fields['name'].choices = state_list

    country= forms.ChoiceField(label="Country",widget=forms.Select(attrs={"class":"form-control"}))
    name= forms.CharField(label="state",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))

class EditCourseForm(forms.Form):
    def __init__(self,course_list,staff_list,courses_code,*args,**kwargs):
        super(EditCourseForm,self).__init__(*args,**kwargs)
        self.fields['course'].choices = course_list
        self.fields['staff'].choices = staff_list
        self.fields['course_code'].choices = courses_code

    course= forms.CharField(label="state",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    course_code= forms.CharField(label="state",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    staff= forms.ChoiceField(label="Staff",widget=forms.Select(attrs={"class":"form-control"}))

#for notice related form
# class addNoticeForm(ModelForm):
#     class Meta:
#         model=Notice
#         fields="__all__"

class addNoticeForm(forms.Form):
    by=forms.CharField(label="By", max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    message=forms.CharField(label="Message",max_length=500,widget=forms.Textarea(attrs={"class":"form-control"}))

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id=kwargs.pop("staff_id")
        super(EditResultForm,self).__init__(*args,**kwargs)
        course_list=[]
        subject_list=[]
        semester_list=[]
        # try:
        #     courses=Courses.objects.filter(staff_id=self.staff_id)
        #     for subject in subjects:
        #         subject_single=(subject.id,subject.subject_name)
        #         subject_list.append(subject_single)
        # except:
        #     subject_list=[]
        try:
            courses=Courses.objects.filter(staff_id=self.staff_id)
            subjects=Subjects.objects.filter(staff_id=self.staff_id)
            semesters=Semesters.objects.all()
            # semesters=Semesters.objects.filter(staff_id=self.staff_id)
            for course in courses:
                course_single=(course.id,course.course_name)
                course_list.append(course_single)
            for subject in subjects:
                subject_single=(subject.id,subject.subject_name)
                subject_list.append(subject_single)
            for semester in semesters:
                semester_single=(semester.id,semester.semesters)
                semester_list.append(semester_single)
        except:
            course_list=[]
            subject_list=[]
            semester_list=[]
        self.fields['course_id'].choices=course_list
        self.fields['subject_id'].choices=subject_list
        self.fields['semester_id'].choices=semester_list

    session_list=[]
    try:
        sessions=SessionYearModel.object.all()
        for session in sessions:
            session_single=(session.id,str(session.session_start_year)+" TO "+str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list=[]

    course_id=forms.ChoiceField(label="Course",widget=forms.Select(attrs={"class":"form-control"}))
    subject_id=forms.ChoiceField(label="Subject",widget=forms.Select(attrs={"class":"form-control"}))
    semester_id=forms.ChoiceField(label="Semester",widget=forms.Select(attrs={"class":"form-control"}))
    session_ids=forms.ChoiceField(label="Session Year",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
    student_ids=ChoiceNoValidation(label="Student",widget=forms.Select(attrs={"class":"form-control"}))
    # exam_months=forms.DateField(label="Exam Months",widget=forms.DateInput(attrs={"class":"form-control"}))
    subject_credits=forms.CharField(label="Subject Credits",widget=forms.TextInput(attrs={"class":"form-control"}))
    internal_marks=forms.CharField(label="Internal Marks",widget=forms.TextInput(attrs={"class":"form-control"}))
    external_marks=forms.CharField(label="External Marks",widget=forms.TextInput(attrs={"class":"form-control"}))

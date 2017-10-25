from django import forms
from .models import Stage1
from phonenumber_field.modelfields import PhoneNumberField


class Stage1Form(forms.ModelForm):
    class Meta:
        model=Stage1
        fields=['Full_name','adharnumber','email']
        #code
    def clean_email(self):
        #adharnumber=self.cleaned_data.get(adharnumber)
        email= self.cleaned_data.get('email')
        email_base,provider=email.split('@')
        domain,extension=provider.split('.')
        if not domain=="aith":
            raise forms.ValidationError("please use your fucked up college id")
        
        #if not extension=='edu':
            #raise forms.ValidationError("please enter the valid .Edu id")
        return email
    #def clean_mobile_number(self):
        #mobile_number=self.cleaned_data.get('mobile_number')
        
        #if not country=="+91":
                #raise form.ValidationError("please fuck yourself and use indian number")
class contactForm(forms.Form):
    
    First_name=forms.CharField(required=False)
    Middle_name=forms.CharField(required=False)
    Last_name=forms.CharField(required=False)
    email=forms.EmailField(required=False)
    phone_number=forms.CharField(max_length=13)
  
    message=forms.CharField(max_length=250)
    
    class Meta:
        model=Stage1
        fields=['phone_number']
        
    
    
class feedbackForm(forms.Form):
    FULL_NAME=forms.CharField(max_length=25,label='Your full name')
    email=forms.EmailField()
    RATING=forms.IntegerField(max_value=5, min_value=0,required=True)
    reason=forms.CharField(max_length=250,label="why you think we are good or bad please explain briefly",required=False)
    contact_number=forms.CharField(max_length=12,label="your personal contact number",required=False)
    
    class Meta:
        model=Stage1
        fields=['RATING,FULL_NAME,contact_number']
        
        
    #code

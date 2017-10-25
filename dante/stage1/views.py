from django.shortcuts import render
from .models import Stage1
from .forms import Stage1Form,contactForm,feedbackForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
      
       
def home(request):
    #title='welcome'
    #if request.user.is_authenticated():
    form=Stage1Form(request.POST or None)
    title='welcome %s' %(request.user)
    
    context={
    'title':title,
    'form':form,
    }
    
    
    if form.is_valid():
        instance=form.save(commit=False)
        if not instance.Full_name:
            instance.Full_name='go kill yourself idiot'
        instance.save()
        print instance.email
        print instance.timestamp
        print instance.adharnumber
        title='Thankyou ! %s' %(request.user)
        context={
            'title':title,
        }
    if request.user.is_authenticated () and request.user.is_staff:
       # print(Stage1.objects.all())
       # i=1
       # for instance in Stage1.objects.all():
        # print(i),
        # print(instance.Full_name)
        # i+=1
        # queryset=Stage1.objects.all().order_by('-timestamp').filter(email__icontains="kill")
        # print(Stage1.objects.all().order_by('-timestamp').filter(email__icontains="kill").count())
        queryset= Stage1.objects.all().order_by('-timestamp')
        print( Stage1.objects.all().order_by('-timestamp').filter(adharnumber__icontains="6").count())
        context={
         "queryset": queryset
          }
    
    return render(request,'home.html',context)

def contact(request):
    form=contactForm(request.POST or None)
    if form.is_valid():
        first=form.cleaned_data.get('First_name')
        last=form.cleaned_data.get('Last_name')
        email=form.cleaned_data.get('email')
        message=form.cleaned_data.get('message')
        number=form.cleaned_data.get('phone_number')
        subject="i am sending you email bitch just bear it!"
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email,'ahmedfalahps3@gmail.com']
        contact_message= "%s: %s via %s"%(first,message,email)
            
        send_mail(subject,contact_message,from_email,[to_email],fail_silently=False)
        
        
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        # 
        #print form.cleaned_data
    title="fill up details along with message our experts will get you soon %s" %(request.user)
    context={
        'title':title,
        'form':form,
    }
    return render(request,'contact.html',context)




def feedback(request):
    form=feedbackForm(request.POST or None)
    if form.is_valid():
        first=form.cleaned_data.get('FULL_NAME')
        email=form.cleaned_data.get('email')
        response=form.cleaned_data.get('response')
        number=form.cleaned_data.get('contact_number')
        # subject="i am sending you email bitch just bear it!"
        # from_email=settings.EMAIL_HOST_USER
        # to_email=[from_email,'ahmedfalahps3@gmail.com']
        # contact_message= "%s: %s via %s"%(first,message,email)
        #     
        # send_mail(subject,contact_message,from_email,[to_email],fail_silently=False)
        
        
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        # 
        #print form.cleaned_data
    title="Have some service  feedback? Tell us what you think %s" %(request.user)
    context={
        'title':title,
        'form':form,
    }
    return render(request,'feedback.html',context)





def profile(request ):
        
    title='welcome to your profile %s' %(request.user)
    context={
    'title':title,
    
    }
    return render(request,'profile.html',context)




from django.shortcuts import render,redirect
from .forms import signupForm,UpdateForm,feedbackForm,milanagentForm,blogreplyForm
from .models import userSignup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from housingsociety import settings
import random
# Create your views here.

def index(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'index.html',{'user':user})



def about(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'about.html',{'user':user})


# @login_required(login_url="/")
def property(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'property.html',{'user':user})
#@login_required(login_url="")
def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cid=userSignup.objects.get(id=uid)
    if request.method=='POST':
        update=UpdateForm(request.POST)
        if update.is_valid():
            update=UpdateForm(request.POST,instance=cid)
            update.save()
            print("Your profile are update successfully")
            return redirect('/property')
        else:
            print(update.errors)
    return render(request,'profile.html',{'user':user,'uid':userSignup.objects.get(id=uid)})

def blog(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'blog.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    if request.method=='POST':
        feedback=feedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            print("your feedback has been sending")

             #Email sending
            # otp=random.randint(1111,9999)
            sub='FEEDBACK'
            msg=f'Feedback\nThank you For your Feedback.\n\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=['chaudharitzz0827@gmail.com']
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('/contact')
        else:
            print(feedback.errors)
    return render(request,'contact.html',{'user':user})


def agentsingle(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'agentsingle.html',{'user':user})

def agentsgrid(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    return render(request,'agentsgrid.html',{'user':user})

def blogsingle(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    if request.method=='POST':
        reply=blogreplyForm(request.POST)
        if reply.is_valid():
            reply.save()
            print("your feedback has been sending")

             #Email sending
            sub='REPLY MESSAGE'
            msg=f'Replay\nThanks for your reply.\n\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=['chaudharitzz0827@gmail.com']
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            
    return render(request,'blogsingle.html',{'user':user})

def propertysingle(request):
    user=request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':       
            signup = signupForm(request.POST)
            if signup.is_valid():
                signup.save()
                print ("user created successfully.")

                #Email sending
                otp=random.randint(1111,9999)
                sub='Wellcome'
                msg=f'HELLO USER\nWellcome to the Housing Society.\nYour one time password is {otp} \nYour Your Account has been created us.\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=['chaudharitzz0827@gmail.com']
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect('/')
            else:
                print (signup.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                return redirect('/property')
    if request.method=='POST':
        milan=milanagentForm(request.POST)
        if milan.is_valid():
            milan.save()
            print("your feedback has been sending")

             #Email sending
            sub='MILAN'
            msg=f'CONTACT\nThanks for you contact me.\n\nEnjoy our services\n\nNeed any Help...\n+91 7990960033 | chaudharitej020@gmail.com'
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=['chaudharitzz0827@gmail.com']
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('/propertysingle')
    return render(request,'propertysingle.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')


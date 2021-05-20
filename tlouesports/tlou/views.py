from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .forms import UserUpdateForm,UserdtlUpdateForm
from .models import News, Games, Ladders, userdtl, Banner, sliders, Social, image, team, \
    Contact, Setting
# from .forms import ContactForm
import random
from django.conf import settings
import threading
from django.core.mail import EmailMessage
# Create your views here.



def detail(request,id):
    team1 = team.objects.get(pk=id)

    context={'team':team1}
    return render(request,'team-details.html',context)

def ranking(request):

    team1=team.objects.get(pk=request.POST.get('team1'))
    team2=team.objects.get(pk=request.POST.get('team2'))
    team.elo_rating(team1,team2,a=1)
    return redirect('home')



class datathread(threading.Thread):
    def __init__(self, data):
        self.data = data
        threading.Thread.__init__(self)

    def run(self):
        self.data.send()


def defhome(request):
    indexnews = News.objects.filter(active=True).order_by('?')
    fBanner = Banner.objects.filter(active=True).order_by('?')[:2]
    fsliders = sliders.objects.filter(active=True).order_by('?')
    fladder = Ladders.objects.filter(active=True).order_by('?')[:4]
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?')[:5]



    teams = team.objects.all().order_by('-points')
    return render(request,'index.html', {'news':indexnews,'banner':fBanner,'slider':fsliders[0],'social':fsocial,'ladder':fladder,'image':fimage ,'teams':teams})

def defnews(request):
    indexnews = News.objects.filter(active=True)[:20]
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    return render(request,'news.html', {'news':indexnews,'social':fsocial,'image':fimage})

def defsnews(request,title):
    indexnews = News.objects.get(title=title)
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    return render(request,'single-blog.html', {'news':indexnews,'social':fsocial,'image':fimage})

def defgames(request):
    games = Games.objects.filter(active=True)[:12]
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    return render(request,'games.html', {'games':games,'social':fsocial,'image':fimage})

def defladders(request,lname):
    sgame = Games.objects.get(Name=lname)
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    ladders = Ladders.objects.filter(game=sgame,active=True)[:12]
    return render(request,'ladders.html', {'gname':lname,'ladders':ladders,'social':fsocial,'image':fimage})

def defladder(request,lname):
    fsocial = Social.objects.all()
    allusr = User.objects.filter(is_staff=False)
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    ladders = Ladders.objects.get(Name=lname,active=True)
    fteam = team.objects.filter(ladder=ladders)
    if request.method == 'POST':
        teamname = request.POST.get('teamname', '')
        tadmin = request.POST.get('tadmin', '')
        mamber1 = request.POST.get('member1', '')
        mamber2 = request.POST.get('member2', '')
        mamber3 = request.POST.get('member3', '')
        mamber4 = request.POST.get('member4', '')
        mamber5 = request.POST.get('member5', '')
        mamber6 = request.POST.get('member6', '')
        mamber7 = request.POST.get('member7', '')
        mamber8 = request.POST.get('member8', '')
        mamber9 = request.POST.get('member9', '')
        mamber10 = request.POST.get('member10', '')
        mamber11 = request.POST.get('member11', '')
        mamber12 = request.POST.get('member12', '')
        mamber13 = request.POST.get('member13', '')
        mamber14 = request.POST.get('member14', '')
        mamber15 = request.POST.get('member15', '')
        try:
            uadmin=User.objects.get(username=tadmin)
        except:
            uadmin=null
        try:
            umamber1=User.objects.get(username=mamber1)
        except:
            umamber1=None
        try:
            umamber2=User.objects.get(username=mamber2)
        except:
            umamber2=None
        try:
            umamber3=User.objects.get(username=mamber3)
        except:
            umamber3=None
        try:
            umamber4=User.objects.get(username=mamber4)
        except:
            umamber4=None
        try:
            umamber5=User.objects.get(username=mamber5)
        except:
            umamber5=None
        try:
            umamber6=User.objects.get(username=mamber6)
        except:
            umamber6=None
        try:
            umamber7=User.objects.get(username=mamber7)
        except:
            umamber7=None
        try:
            umamber8=User.objects.get(username=mamber8)
        except:
            umamber8=None
        try:
            umamber9=User.objects.get(username=mamber9)
        except:
            umamber9=None
        try:
            umamber10=User.objects.get(username=mamber10)
        except:
            umamber10=None
        try:
            umamber11=User.objects.get(username=mamber11)
        except:
            umamber11=None
        try:
            umamber12=User.objects.get(username=mamber12)
        except:
            umamber12=None
        try:
            umamber13=User.objects.get(username=mamber13)
        except:
            umamber13=None
        try:
            umamber14=User.objects.get(username=mamber14)
        except:
            umamber14=None
        try:
            umamber15=User.objects.get(username=mamber15)
        except:
            umamber15=None
        
        pteam = team(Name=teamname,ladder=ladders,Member1=uadmin,Member2=umamber2,Member3=umamber3,Member4=umamber4,Member5=umamber5,Member6=umamber6,Member7=umamber7,Member8=umamber8,Member9=umamber9,Member10=umamber10,Member11=umamber11,Member12=umamber12,Member13=umamber13,Member14=umamber14,Member15=umamber15)
        pteam.save()
        messages.success(request, "Your team has been successfully created")
        return redirect("/ladder/"+str(ladders.Name))
    return render(request,'ladder.html', {'ladder':ladders,'social':fsocial,'image':fimage,'alluser':allusr,'team':fteam})

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        psn = request.POST['psn']
        xbl = request.POST['xbl']
        # Check for errorneous inputs
        if User.objects.filter(username=username):
            messages.error(request, "Username you choose is already used")
            return redirect('/')
        # username should be under 10 characters
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters")
            return redirect('/')
        
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('/')

        # passwords should match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')

        # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        dtluser = userdtl(user_id = myuser.id, tpass = random.randint(1000,9999), bpass = pass1, psn=psn, xbl=xbl)
        dtluser.save()
        messages.success(request, "Your Tlouesports account has been successfully created")
        return redirect("/validate/"+ myuser.username +"")
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        if loginpassword == "":
            return redirect("/validate/"+ loginusername +"")

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/') 
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')
            
    return HttpResponse('404 - Not Found')


def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/') 


def validate(request, user):
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    try:
        vuser = User.objects.get(username = user)
        email_from = settings.EMAIL_HOST_USER
        msg = EmailMessage(
            "Your code for tlouesports.com is Generated",
            "Hi " + vuser.first_name + ", <br><br> Your code for tlouesports.com is "+ vuser.userdtl.tpass + "<footer> <br><br><hr> Do not share this code with anyone <br><hr> Thank you for using tlouesports.com! </footer>",
            email_from,
            [vuser.email],
        )
        msg.content_subtype = "html"
        datathread(msg).start()
        if request.method == "POST":
            passw = request.POST['onepass']
            if passw == vuser.userdtl.tpass:
                musr = User.objects.get(username = user)
                if musr.is_active == False:
                    musr.is_active = True
                    messages.success(request, "Account Validation Successful !")
                else:
                    passn = request.POST['npass']
                    musr.set_password(passn)
                    usr = userdtl.objects.get(user = musr)
                    usr.bpass = passn
                    usr.save()
                    messages.success(request, "Password changed successfully !!")
                musr.save()
                login(request, musr)
            
                return redirect("/")
            else:
                messages.success(request, "Invalid OTP")
    except:
        messages.error(request, "Account not Exists")
        return redirect('/')
    return render(request, 'validate.html', {'vuser': vuser,'social':fsocial,'image':fimage})


def defprofile(request, user):
    fsocial = Social.objects.all()
    fimage = image.objects.filter(active=True).order_by('?'[:5])
    try:
        vuser = User.objects.get(username = user)
        if vuser != request.user:
            messages.error(request,"You are not allow to access profile of other user")
            return redirect("/")
    except:
        messages.error(request,"You are trying to access profile of Invalid user")
        return redirect("/")
    return render(request,'profile.html',{'user':vuser,'social':fsocial,'image':fimage})

@csrf_exempt
def defcontact(request):
    setting = Setting.objects.get(pk=2)
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        ip = request.META.get('REMOTE_ADDR')
        contact= Contact(name=name, phone=phone, email=email, desc=desc, ip=ip, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")


    context = {'setting': setting}
    return render(request,'contact.html', context)

@login_required(login_url='/login') # Check login
@csrf_exempt
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        userdtl_form = UserdtlUpdateForm(request.POST, instance=request.user.userdtl)
        if user_form.is_valid() and userdtl_form.is_valid():
            user_form.save()
            userdtl_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/')
    else:
        user_form = UserUpdateForm(instance=request.user)
        userdtl_form = UserdtlUpdateForm(instance=request.user.userdtl)
        context = {
            'user_form': user_form,
            'userdtl_form': userdtl_form
        }
        return render(request, 'profile.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting}
    return render(request, 'about.html', context)

import math


def EloRating(Ra, Rb, a, t1c=False, t2c=False):
    if a == 1:
        if Ra < 1500:
            K = 50
        elif 1500 <= Ra < 1800:
            K = 40
        elif Ra >= 1800:
            K = 25
    else:
        if Rb < 1500:
            K = 50
        elif 1500 <= Rb < 1800:
            K = 40
        elif Rb >= 1800:
            K = 25

    Pb = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (Ra - Rb) / 400))
    Pa = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (Rb - Ra) / 400))
    if (a == 1):
        New_t1 = Ra + K * (1 - Pa)
        New_t2 = Rb + K * (0 - Pb)
    else:
        New_t1 = Ra + K * (0 - Pa)
        New_t2 = Rb + K * (1 - Pb)

    if t1c:
        if a == 1:
            pts = New_t1 - Ra
            New_t1 += pts
        else:
            t1c = False
            t2c = True
    elif t2c:
        if a != 1:
            pts = New_t2 - Rb
            New_t2 += pts
        else:
            t1c = True
            t2c = False

    return New_t1, New_t2, t1c, t2c
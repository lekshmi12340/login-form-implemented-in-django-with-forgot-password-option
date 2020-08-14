from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


from .forms import signupform,resetform
from .models import user,resetpassword


def signup(request):
    form=signupform()
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            loginid = form.cleaned_data['loginid']
            request.session['loginid'] = loginid
            password = form.cleaned_data['password']
            emailaddress = form.cleaned_data['emailaddress']
            phonenumber = form.cleaned_data['phonenumber']

            users=user()
            users.name=name
            users.loginid=loginid
            users.password=password
            users.emailaddress=emailaddress
            users.phonenumber=phonenumber

            users.save()
            return render(request,'loginapp/success.html',{'form':form})


    return render(request,'loginapp/signup.html',{'form':form})
def login(request):
    if request.method=="POST":
        loginid=request.POST.get("loginid")
        password=request.POST.get("password")

        userdata=user.objects.filter(loginid=loginid,password=password)
        if userdata:
            form=signupform()
            return render(request,'loginapp/welcome.html',{'loginid':loginid})

    return render(request,'loginapp/index.html')
def resetpasswords(request):
    form=resetform()
    if request.method=='POST':
        form=resetform(request.POST)
        if form.is_valid():
            yourloginid = form.cleaned_data['yourloginid']
            enterpassword = form.cleaned_data['enterpassword']
            confirmpassword = form.cleaned_data['confirmpassword']
            resep = user.objects.get(loginid=yourloginid)

            resep.password = enterpassword

            resep.save()
            return render(request, 'loginapp/passwordreset.html', {'yourloginid': yourloginid})
    return render(request, 'loginapp/reset.html', {'form': form})

def logout(request):
    return render(request,'loginapp/logout.html')

def redirects(request):
    if request.method=='POST':
        loginid = request.POST.get("loginid")
        remember_me=request.POST.get("remember_me")
        userdata=user.objects.filter(loginid=loginid)
        if userdata:
            return render(request,'loginapp/welcome.html',{'loginid':loginid})
    return render(request,'loginapp/redirect.html')
























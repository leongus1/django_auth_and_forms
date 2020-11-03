from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from login_app.forms import UserCreateForm, loginForm
import bcrypt


# Create your views here.
def index(request):
    regForm = UserCreateForm()
    users = User.objects.all()
    login = loginForm()
    context = {
        'registrationForm': regForm,
        'users': users,
        'login': login
    }
    return render(request, 'index.html', context)

def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form2 = UserCreateForm(request.POST)
    if form2.is_valid():
        user = form2.save(commit=True)
        user.save()
        print("user is now saved", request.POST['first_name'], "or user:", user.first_name)
        request.session['name'] = request.POST['first_name']
    
        return redirect('/success')
    print('user not valid')
    return redirect('/')

def auth_log(request):
    if request.method=='POST':
        if len(User.objects.filter(username=request.POST['email']))==1:
            user1 = User.objects.get(username=request.POST['email'])
            testuser = authenticate(username=request.POST['email'], password=request.POST['password'])
            login(request, user1)
            if testuser:
                request.session['name']=user1.first_name
                return redirect('/success')
    
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

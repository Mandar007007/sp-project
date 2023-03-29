from django.shortcuts import render,redirect
from myapp.models import Account,Teacher

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        if Account.objects.filter(username=username).exists():
            return redirect('/myapp')
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        email = request.POST['email']

        role = 1

        if role == 'u':
            new_account = Account(username=username,password=password1,email=email,userrole=0)
        else:
            new_account = Account(username=username,password=password1,email=email,userrole=1)
        new_account.save()
        
        return redirect('/myapp/register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        
        if Account.objects.filter(username=username).exists():
            my_obj = Account.objects.get(username=username)
            if password == my_obj.password:  
                userrole = Account.objects.get(username=username).userrole
                email = Account.objects.get(username=username).email
                request.session['loggedin'] = True
                request.session['name'] = username
                request.session['role'] = userrole
                request.session['email'] = email
                
                return redirect('/myapp/')
                return render(request,'home.html',dir)
                return render(request,'register.html',dir)
    else:
        return render(request,'register.html')
    return render(request,'register.html')

def about(request):
    return render(request,'demo.html')

def leaderboard(request):
    teachers = Teacher.objects.all().order_by('-score')
    return render(request,'leaderboard.html',{'teachers':teachers})

def rate(request):
    username = request.POST['id']
    check = request.POST.getlist('check')
    if(check):
        obj = Teacher.objects.get(username=username)
        obj.score = obj.score+1
        obj.save()
    return redirect('/myapp/leaderboard')

def logout(request):
    request.session.flush()
    return redirect('/myapp')



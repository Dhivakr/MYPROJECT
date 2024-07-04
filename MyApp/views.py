from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import userCustomForm,Created_form
from .models import TaskCreated


# Create your views here.

def home(request):
    return render(request,'index.html')

def dhashboard(request):
    return render(request,'LoginAndregister/dhashboard.html')

def register(request):
    form=userCustomForm()
    if request.method=='POST':
        form=userCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_page')
    return render(request,'LoginAndregister/register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        redirect('/dhashboard')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('/dhashboard')
            else:
                return redirect('/login_page')
    return render(request,'LoginAndregister/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def create_task(request):
    if request.method == 'POST':
        form = Created_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dhashboard')
    else:
        form =Created_form()
    return render(request,'Task/create_task.html',{'form':form})



def view_task(request):
    views_datas=TaskCreated.objects.all()
    return render(request,'Task/view_task.html',{'views_datas':views_datas})



def delete(request,pk):
    item = get_object_or_404(TaskCreated,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/dhashboard')
    return render(request, 'Task/delete.html',{'item':item})

def update(request,pk):
    instance = get_object_or_404(TaskCreated,pk=pk)
    if request.method == 'POST':
        form = Created_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    else:
        form = Created_form(instance=instance)
    return render(request, 'Task/create_task.html',{'form':form})


def detail_view(request, pk):
    task_view= get_object_or_404(TaskCreated, id=pk)
    return render(request,'Task/fulltaskview.html',{'task_view':task_view})


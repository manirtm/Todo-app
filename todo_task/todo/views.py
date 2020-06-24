from django.shortcuts import render
import pdb
from .models import User, Task

# Create your views here.

def get_task():
    task_ = []
    dict_ = {}
    tasks = Task.objects.all()
    for task in tasks:
        title = task.title
        status = task.status
        username = task.user.username
        user_id = task.user_id
        id_ = task.id
        dict_['title'] = title
        dict_['status'] = status
        dict_['username'] = username
        dict_['user_id'] = user_id
        dict_['task_id'] = id_
        task_.append(dict_)
        dict_  = {}
    return task_


def register(request):
    if request.POST:
        form = request.POST
        username = form['username']
        password = form['password']        
        user_object = User.objects.filter(username=username)
        if user_object.exists():
            return render(request, 'login.html')
        user_create = User.objects.create(username=username, password=password)
        context = {"data": 'User Registered Successfully, Login now'}
        return render(request, 'login.html', context)
    return render(request, 'register.html')

def login(request):
    if request.POST:
        form = request.POST
        username = form['username']
        password = form['password']
        user_object = User.objects.filter(username=username)
        if user_object.exists():
            task_ = get_task()
            if  user_object[0].password == password:
                context = { "data": task_}
                return render(request, template_name =  'grid.html', context=context)
        return render(request, 'login.html')
    return render(request, 'login.html')


def create(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        status= request.POST.get('status')
        user_id= request.POST.get('user_id')
        task = Task(title=title, status=status,user_id=user_id)
        task.save()
        task_ = get_task()
        if task_:
            context = {"data": task_}
            return render(request, template_name='grid.html', context=context)
    users = list(User.objects.values())
    context = {"data":users}
    return render(request,template_name= 'create.html', context=context)

def reopen(request, id):
    task_reopen = Task.objects.filter(id=id).update(status='open')
    task_ = get_task()
    if task_:
        context = {"data": task_}
        return render(request, template_name='grid.html', context=context)
    return render(request, template_name='grid.html')

def edit(request, id):
    if request.method == 'POST':
        form = request.POST
        title = form['title']
        status = form['status']
        user_id = form['user_id']
        task_reopen = Task.objects.filter(id=id).update(status=status, user_id=user_id, title=title)
        tasks = get_task()
        context = {"data": tasks}
        return render(request, template_name='grid.html', context=context)
    task_edit = Task.objects.filter(id=id)
    edit_details ={}
    if task_edit.exists():
        task_id = task_edit[0].id
        title = task_edit[0].title
        status = task_edit[0].status
        user_id = task_edit[0].user_id
        edit_details['task_id'] = task_id
        edit_details['title'] = title
        edit_details['status'] = status
        edit_details['user_id'] = user_id
        users = list(User.objects.values())
        context = {"data": edit_details, "users": users}
        return render(request, template_name='edit.html', context=context)
    return render(request, template_name='edit.html')

def delete(request, id):
    task_reopen = Task.objects.filter(id=id).delete()
    task_ = get_task()
    if task_:
        context = {"data": task_}
        return render(request, template_name='grid.html', context=context)
    return render(request, template_name='grid.html')

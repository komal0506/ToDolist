from django.shortcuts import redirect, render , HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success':False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title , taskDescription=desc)
        ins.save()
        context = {'success':True}
    
    return render (request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context ={'tasks': allTasks}
    return render (request, 'tasks.html', context)

def delete(request, title):
    get_todo=Task.objects.get(taskTitle=title)
    get_todo.delete()
    return redirect('/')
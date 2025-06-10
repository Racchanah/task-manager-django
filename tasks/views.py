from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request,'tasks/task_list.html',{'tasks':tasks,'form':form})


from django.shortcuts import get_object_or_404

def edit_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request,'tasks/edit_task.html',{'form':form})

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
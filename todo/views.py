from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Task
from .forms import TaskForm

# Create your views here.

# Goes to index page
def index(request):
    context = {}

    # Checking if asked to filter tasks based on completion
    if request.session.has_key('completed'):

        # request.session['completed'] is either True or False
        context['tasks'] = Task.objects.filter(Completed=request.session.get('completed'))

        # Pass completed/unfinished tag to index.html
        if request.session.get('completed'):
            context['completed'] = "True"
        else:
            context['unfinished'] = "True"
        
        try:
            del request.session['completed']        # delete request.session['completed']
        except KeyError:
            pass
    
    # If no 'complete' filter option get all tasks
    else:
        context['tasks'] = Task.objects.all()

    return render(request, 'todo/index.html', context)

# To get completed Tasks
# Redirect to index() view with request.session['completed'] = True
def get_completed(request):
    request.session['completed'] = True
    return HttpResponseRedirect(reverse('todo:index'))

# To get unfinished tasks
# Redirect to index() view with request.session['completed'] = False
def get_unfinished(request):
    request.session['completed'] = False
    return HttpResponseRedirect(reverse('todo:index'))

# Adding a task
def add(request):
    # if POST data sent from a form
    if request.POST:
        form = TaskForm(request.POST)
        form.save()
        success_message = "'" + request.POST['Title'] + "' Created Successfully"
        messages.success(request, success_message)
        return HttpResponseRedirect(reverse('todo:index'))
    # else if no data create an empty form
    else:
        form = TaskForm()
        form.helper.form_action = "add"
        return render(request, 'todo/add_task.html', {'form': form})

# Editing a task
def edit(request, identifier):
    # if POST data sent by form
    if request.POST:
        form = TaskForm(request.POST)
        form.save()
        success_message = "Task " + request.POST['Title'] + "' Updated Successfully "
        messages.success(request, success_message)
        return HttpResponseRedirect(reverse('todo:index'))
    # else create a form and fill form with task data for editing
    else:
        task = get_object_or_404(Task, id=identifier)
        form = TaskForm(instance=task)
        form.helper.form_action = reverse('todo:edit', args=[task.id,])
        return render(request, 'todo/edit_task.html', {'form':form})

#Delete a task
def delete(request, identifier):
    task = get_object_or_404(Task, id=identifier)

    task.delete()
    success_message = 'Task ' + task.Title + ' Deleted Successfully'
    messages.error(request, success_message)
    return HttpResponseRedirect(reverse('todo:index'))

def complete(request, identifier):
    task = get_object_or_404(Task, id=identifier)

    task.Completed = True
    task.save()
    success_message = "'" + task.Title + "' Completed"
    messages.success(request, success_message)
    return HttpResponseRedirect(reverse('todo:index'))

def remove_complete(request, identifier):
    task = get_object_or_404(Task, id=identifier)

    task.Completed = False
    task.save()
    success_message = "'" + task.Title + "' removed from Completed Tasks"
    messages.success(request, success_message)
    return HttpResponseRedirect(reverse('todo:index'))
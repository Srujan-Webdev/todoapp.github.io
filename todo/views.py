from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm, TaskUpdateForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from datetime import date
from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    # return HttpResponse("Todo App")

    # Getting all objects of "Task" Model(declared in "models.py") from "Database"
    #todo_items = Task.objects.all()
    todo_items = Task.objects.filter(user=request.user)

    # Counting number of "todo_items" present in "Database"
    count_todo_items = todo_items.count()

    # For finding completed tasks
    completed_todo = Task.objects.filter(user=request.user, completed=True)
    count_completed_todo = completed_todo.count()

    # For finding uncompleted tasks
    count_uncompleted_todo = count_todo_items - count_completed_todo

    # Validating the "content" in "TaskForm"("POST" and "GET" methods)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save()
            #or(Here we are not saving the form as we mentioned commit=False, as form doesn't contain the "user" information, we are mentioning the user and then saving it, if we don't mention the user now, form will take "admin"/"superuser" as user)
            todo_save = form.save(commit=False)         #Here we are referencing the "form object" and adding the "user" to "form"
            todo_save.user = request.user
            todo_save.save()
            return redirect('/')
    else:
        form = TaskForm()

    #Searching functionality starts
    if 'q' in request.GET:
        q = request.GET['q']
        #todo_items = Task.objects.filter(content__icontains=q)
        #or
        multiple_q = Q(Q(content__icontains=q) | Q(content__icontains=q))
        todo_items = Task.objects.filter(multiple_q, user=request.user)
    #Searching functionality ends

    # Pagination - Starts
    todo_paginator_obj = Paginator(todo_items, 3)
    todo_page_number = request.GET.get("page")
    # or
    #todo_page_number = request.GET["page"]
    todo_page = todo_paginator_obj.get_page(todo_page_number)
    # Pagination - Ends

    #sendmail()

    # Creating Dictionary sothat all things can be to send at a time to "index.html"
    context = {'todo_items': todo_items,
               'form': form,
               'todo_page': todo_page,
               'count_todo_items': count_todo_items,
               'count_completed_todo': count_completed_todo,
               'count_uncompleted_todo': count_uncompleted_todo,
               }

    return render(request, 'todo/index.html', context)

#Sending mail
def sendmail():
    todo_items = Task.objects.all()
    #print("sending mail success")
    #sending mail starts
    for i in todo_items:
        if i.completed==False:
            j = i.time_tobe_completed - date.today()        
            if 1<=j.days<=7:
                send_mail(
                '{}'.format(i.content),#subject
                '{} days more to complete'.format(j.days),#Body of the mail
                'srs.webdev.superuser@gmail.com',#from mail
                ['srs.webdev.2@gmail.com'],#to mail list
                fail_silently=False,#will throw error if mail has not sent
    )
    #sending mail ends

def update(request, pk):

    todo_item_to_be_modify = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=todo_item_to_be_modify)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskUpdateForm(instance=todo_item_to_be_modify)

    context = {
        'form': form,
    }

    return render(request, 'todo/update.html', context)


def delete(request, pk):
    todo_item_to_be_deleted = Task.objects.get(id=pk)

    if request.method == 'POST':
        todo_item_to_be_deleted.delete()
        return redirect('/')

    return render(request, 'todo/delete.html')

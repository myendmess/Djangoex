from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    tasks = request.session.get("tasks", [])  # Retrieve tasks from the session or provide an empty list
    form = NewTaskForm()

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)  # Append the task to the tasks list

            request.session["tasks"] = tasks  # Update tasks in the session

            return HttpResponseRedirect(reverse("tasks:index"))  # Redirect to the index view

    return render(request, "tasks/index.html", {
        "tasks": tasks,
        "form": form
    })

def add(request):
    form = NewTaskForm()
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks = request.session.get("tasks", [])  # Retrieve tasks from the session or provide an empty list
            tasks.append(task)  # Append the task to the tasks list
            request.session["tasks"] = tasks  # Update tasks in the session
            return HttpResponseRedirect(reverse("tasks:index"))  # Redirect to the index view
    
    return render(request, "tasks/add.html", {
        "form": form
    })

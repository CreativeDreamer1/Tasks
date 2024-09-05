from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TaskForm

# This is the main page of the application where all the tasks will be displayed
# It will display 2 properties of the tasks: 1) the title 2) the description

def index(request):

    # Declaring "tasks" and "descriptions" as list
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if "descriptions" not in request.session:
        request.session["descriptions"] = []

    # Store it in variables (for simplicity)
    tasks = request.session["tasks"]
    desc = request.session["descriptions"]

    # Context (for template)
    n = list(zip(tasks, desc))
    return render(request, "tasks/index.html", {
        "n" : n
    })

# This function adds the new task with descriptions
# After submitting it will return user to the main page where they can view tasks

def add(request):

 	# Check if user posted anything
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # Check if the length of the data is within the range
        if form.is_valid():

            # Accessing the new task and description that user posted and storing them
            task = form.cleaned_data["task"]
            description = form.cleaned_data["description"]

            # Accessing the list of tasks and descriptions of user
            tasks = request.session["tasks"]
            descriptions = request.session["descriptions"]

            # Adding the new task and descriptions in the list
            tasks.append(task)
            descriptions.append(description)

            # Storing the new lists in orignal list of tasks and descriptions
            request.session["tasks"] = tasks
            request.session["descriptions"] = descriptions

            # Redirecting user to the main page where tasks are displayed
            return HttpResponseRedirect(reverse("tasks:index"))
    
    # If the user has not posted anything then return the form for tasks
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {
        "form" : form,
    })

# This function deletes the task by taking task id as a parameter
# This can aslo be done by editing the url (as seen in the urls.py file)

def delete(request, task_id):

    # Ensuring it only works if tasks and descriptions list are not empty
    if ("tasks" in request.session) and ("descriptions" in request.session):

        # Accessing all the list of tasks and descriptions
        tasks = request.session["tasks"]
        descriptions = request.session["descriptions"]

        # If the task id given is within the index of the list
        if 0 <= task_id < len(tasks):

            # Remove the task and description using its index
            tasks.pop(task_id)
            descriptions.pop(task_id)

            # Storing the new list in the user sessions
            request.session["tasks"] = tasks
            request.session["descriptions"] = descriptions

    # Return the user to the main page where tasks are displayed
    return redirect('tasks:index')


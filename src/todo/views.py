from django.shortcuts import render


def home(request):
    return render(request, "todo/home.html")


def todolist(request):
    todos = Todo.objects.all()

# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from todos.models import TodoList

# Create your views here.
class TodoListListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"

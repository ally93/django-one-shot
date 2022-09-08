from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from todos.models import TodoList

# Create your views here.
class TodoListListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/edit.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"

    def get_success_url(self):
        return reverse_lazy("todo_list_list")

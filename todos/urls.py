from django.urls import path

from todos.views import (
    TodoListListView
)

urlpatterns = [
    path("", TodoListListView.as_view(), name="todo_list_list")
]

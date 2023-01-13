from django.views.generic import DetailView, ListView

from todo.models import TodoModel


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
    context_object_name = 'todo_list'


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    context_object_name = 'todo_detail'

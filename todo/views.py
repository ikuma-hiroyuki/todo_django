from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from todo.models import TodoModel


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
    context_object_name = 'todo_list'


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    context_object_name = 'todo_detail'


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')  # html上でどのフィールドを表示するか指定
    success_url = reverse_lazy('list')  # todoのurls.pyのname='list'を指定


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

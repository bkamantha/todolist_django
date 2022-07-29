from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .models import Task


class TaskList(ListView):
    model = Task
    # template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'detail_task'


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')

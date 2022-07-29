from asyncio import tasks
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task


class TaskList(ListView):
    model = Task
    # template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'detail_task'

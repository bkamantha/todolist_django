from django.http import HttpResponse


def taskList(request):
    return HttpResponse('todo list')

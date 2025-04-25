from celery import shared_task
from rest_framework.generics import get_object_or_404
from .models import Task

@shared_task
def sum(id: int):
    try:
        task = get_object_or_404(Task, id=id)
        result = task.first_value + task.second_value
        task.result = result
        task.save()
        return {"resultado": f"task finalizada, resultado: {task.result}"}
    except Exception as ex:
        return str(ex)
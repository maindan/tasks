from celery import shared_task

@shared_task
def sum(x, y):
    return x + y
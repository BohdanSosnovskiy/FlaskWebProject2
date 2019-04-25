"""Include modul"""
from celery import Celery

CELERY = Celery('tasks',
                broker="amqp://guest@localhost//",
                backend="amqp://guest@localhost//", ignore_result=False)

@CELERY.task
def add(num1, num2):
    """Function summer"""
    return num1 + num2

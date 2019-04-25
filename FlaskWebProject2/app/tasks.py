from celery import Celery

celery = Celery('tasks',
                broker="amqp://guest@localhost//",
                backend="amqp://guest@localhost//", ignore_result=False)

@celery.task
def add(num1, num2):
    return num1 + num2

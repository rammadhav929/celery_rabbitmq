from celery import shared_task
import time

a = 1


@shared_task
def test_task():
    a += 1
    print("Task started " + str(a))
    time.sleep(5)
    print("Task completed")
    return "done"


@shared_task
def add(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y

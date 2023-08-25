from time import sleep
from celery import shared_task

@shared_task
def notify_customer(message):
    print("sending message to customer...")
    print(message)
    sleep(10)
    print("message sent to customer")
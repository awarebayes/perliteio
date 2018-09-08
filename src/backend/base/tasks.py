from celery import shared_task
from . import models
from datetime import date
import time
import random

CHRISTMAS = date(1, 1, 1)


@shared_task
def check_solution(pk):
    ticket_object = models.Ticket.objects.get(pk=pk)

    # Do what you want with the ticket
    ticket_object.age = (ticket_object.born - CHRISTMAS).days
    random.seed(ticket_object.age)
    ticket_object.prize = random.randint(1, 10000)
    print("".join(["name: ", str(ticket_object.name), " ->age: ", str(ticket_object.age), " ->prize: ", str(ticket_object.prize)]))
    time.sleep(5)

    ticket_object.save()


from django.db import models
from django.dispatch import receiver
from .tasks import check_solution


class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False)
    born = models.DateField()
    age = models.IntegerField(default=-1)
    prize = models.IntegerField(default=-1)


@receiver(models.signals.post_save, sender=Ticket)
def solution_execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        check_solution.apply_async([instance.id])

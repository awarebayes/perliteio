from django.shortcuts import render
from django.apps import apps

from django.http import HttpResponseRedirect

def landing(request):
    Tickets = apps.get_model('base', 'Ticket')
    wins = Tickets.objects.filter(age__gt=0).order_by('-pk')[:9]
    wins = [wins[i:i + 3] for i in range(0, len(wins), 3)]
    return render(request, 'landing.html', {'wins': wins})


def delete(request):
    Tickets = apps.get_model('base', 'Ticket')
    Tickets.objects.all().delete()
    return HttpResponseRedirect("/")

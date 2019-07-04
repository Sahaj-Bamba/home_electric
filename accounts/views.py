from django.shortcuts import render
from datetime import date
from .models import *
# Create your views here.


def user_room(request):
    y = 0
    if request.method == 'POST':
        data = int(request.POST.copy().get('hidden_room'))
        y = data
        request.session['room_number'] = data
    x = user_details.objects.get(user_room_no=y)
    z = date.today().day

    if x.user_date_entry == date.today().day:
        if x.billed == 0:
            prepare_bill(x)
            x.billed = 1
            x.save()
    z = date.today().month

    return render(request, 'accounts\\room.html', {'test': z})


def prepare_bill(x):
    pass
from django.shortcuts import render,redirect
from datetime import date
from .models import *
# Create your views here.

# 28 is re billing set date


def own(request):

    return render(request, 'accounts/own.html')


def user_room(request):
    y = 0
    if request.method == 'POST':
        data = int(request.POST.copy().get('hidden_room'))
        y = data
        request.session['room_number'] = data
        # //abc=data+1
    if y==0:
        return redirect('home')
    x = user_details.objects.get(user_room_no=y)

    z = date.today().day
    abc=1
    if z == 28:
        abc=5
        x.billed = 1
        x.save()
    abc=x.user_date_entry
    if x.user_date_entry == date.today().day:
        if x.billed == 1:

            # bill preparation script

            ze = bill.objects.filter(room_no=x.user_room_no).order_by("-dob").first()
            if ze is None:
                x.previous_dues = 0
            else:
                x.previous_dues = ((ze.dues + ze.rent + ze.electric_bill) - ze.payed);

            a = bill()

            a.room_no = x.user_room_no
            a.dues = x.previous_dues
            a.rent = x.user_rent

            b = consumption.objects.filter(room_no=x.user_room_no).order_by("-dor").order_by("-reading")

            if b is None:
                a.electric_bill = 0
            else:
                a.electric_bill = (b.first().reading - x.previous_units)*6
                x.previous_units = b.first().reading

            a.dob = date.today()
            a.payed = 0

            x.previous_dues = a.dues + a.rent + a.electric_bill
            x.billed = 0

            a.dob = date.today()

            x.save()
            a.save()

            # bill prepared

        else:
            a = bill.objects.filter(room_no=x.user_room_no).order_by("-dob").first()
            pass
    else:
        a = bill.objects.filter(room_no=x.user_room_no).order_by("-dob").first()
        pass
    if a is None:
        return redirect('home')
    else:
        return render(request, 'accounts/room.html', {'dues': a.dues, 'rent': a.rent, 'electric': a.electric_bill, 'payed':a.payed ,'total': ((a.dues+a.rent+a.electric_bill)-a.payed)})


def user_login(request):
    if request.method == 'POST':
        data = request.POST.copy()
        a = data.get('name')
        b = data.get('pass')
        x = my_users.objects.filter(my_user_name=a).filter(my_user_pass=b)
        if x.count() > 0:
            request.session['gamer'] = a
            request.session['gamer_auth'] = x.first().authority
            return redirect('home')

    return render(request, 'accounts/login.html')
    pass


def pay(request):
    if request.method == 'POST':
        data = request.POST.copy()
        a = data.get('a')
        b = data.get('b')
        x = bill.objects.filter(room_no=a).order_by("-dob").first()
        x.payed += int(b)
        x.save()

        y = payment()
        y.room_no = a
        y.amount = b
        y.dop = date.today()
        y.save()
        return redirect('accounts:room')
        pass

    return render(request, 'accounts/pay.html')
    pass


def user_logout(request):
    if request.method == 'POST':
        del request.session['gamer']
        del request.session['gamer_auth']

    return redirect('home')
from django.db import models
from django.contrib.auth.models import User


class my_users(models.Model):
    my_user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    authority = models.IntegerField(verbose_name="authority", default=0)
    my_user_pass = models.CharField(verbose_name="pass", max_length=100, blank=False)


class user_details(models.Model):

    user_room_no = models.DecimalField(verbose_name="room_no", max_digits=2, decimal_places=0, blank=False, default=0)
    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_date_entry = models.IntegerField(verbose_name="date_entry", default=0)
    user_doj = models.DateField(verbose_name="doj")
    user_contact = models.IntegerField(verbose_name="contact", default=0)
    user_rent = models.DecimalField(verbose_name="rent", max_digits=10, decimal_places=2, blank=False, default=0)
    previous_units = models.DecimalField(verbose_name="prev_units", max_digits=10, decimal_places=2, blank=False, default=0)
    previous_dues = models.DecimalField(verbose_name="prev_dues", max_digits=10, decimal_places=2, blank=False, default=0)
    billed = models.IntegerField(verbose_name="billed", default=0)

    def __str__(self):
        return str(self.user_room_no) + self.user_name


class consumption(models.Model):
    room_no = models.IntegerField(verbose_name="room", default=0)
    reading = models.DecimalField(verbose_name="reading", max_digits=10, decimal_places=1, blank=False, default=0.0)
    dor = models.DateField(verbose_name="dor")


class payment(models.Model):
    room_no = models.IntegerField(verbose_name="room")
    amount = models.DecimalField(verbose_name="amount", max_digits=10, decimal_places=1, blank=False, default=0)
    dop = models.DateTimeField(verbose_name="dop")


class bill(models.Model):
    room_no = models.IntegerField(verbose_name="room")
    payed = models.DecimalField(verbose_name="payed", max_digits=10, decimal_places=2, blank=False)
    dues = models.DecimalField(verbose_name="dues", max_digits=10, decimal_places=2, blank=False)
    rent = models.DecimalField(verbose_name="rent", max_digits=10, decimal_places=2, blank=False)
    electric_bill = models.DecimalField(verbose_name="electric_bill", max_digits=10, decimal_places=2, blank=False)
    dob = models.DateField(verbose_name="dob")
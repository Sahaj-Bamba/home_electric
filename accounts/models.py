from django.db import models
from django.contrib.auth.models import User


class my_users(models.Model):
    my_user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    authority = models.IntegerField(verbose_name="authority", default=0)
    my_user_pass = models.CharField(verbose_name="pass", max_length=100, blank=False)


class user_details(models.Model):
    user_room_no = models.DecimalField(verbose_name="room_no", max_digits=2, decimal_places=0, blank=False)
    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_date_entry = models.IntegerField(verbose_name="date_entry", default=0)
    user_doj = models.DateTimeField(verbose_name="doj")
    user_contact = models.IntegerField(verbose_name="contact", default=0)
    rent = models.DecimalField(verbose_name="rent", max_digits=10, decimal_places=2, blank=False)
    bill_prep = models.IntegerField(verbose_name="bill_prep", default=0)

    def __str__(self):
        return str(self.user_room_no) + self.user_name


class consumption(models.Model):
    room_no = models.IntegerField(verbose_name="room")
    reading = models.DecimalField(verbose_name="reading", max_digits=10, decimal_places=1, blank=False)
    dor = models.DateTimeField(verbose_name="dor", auto_now_add=True)


class payment(models.Model):
    room_no = models.IntegerField(verbose_name="room")
    amount = models.DecimalField(verbose_name="amount", max_digits=10, decimal_places=1, blank=False)
    dop = models.DateTimeField(verbose_name="dop", auto_now_add=True)


class bill(models.Model):
    room_no = models.IntegerField(verbose_name="room")
    dues = models.DecimalField(verbose_name="dues", max_digits=10, decimal_places=2, blank=False)
    rent = models.DecimalField(verbose_name="rent", max_digits=10, decimal_places=2, blank=False)
    electric_bill = models.DecimalField(verbose_name="electric_bill", max_digits=10, decimal_places=2, blank=False)
    dob = models.DateTimeField(verbose_name="dob", auto_now_add=True)


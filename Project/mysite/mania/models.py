
from itertools import count
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import models


class Account(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Undefined", "Undefined"),
    )
    phone_number = PhoneNumberField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        

class Court(models.Model):
    court_name = models.CharField(max_length=200)
    court_address = models.CharField(max_length=200)
    contact_number = PhoneNumberField(blank=True, null=True)
    
    court_admin = models.ForeignKey(Account, on_delete=models.CASCADE)
    court_fee = models.IntegerField()
    upload_court_pictures = models.ImageField(upload_to ='court_photos')

    def __str__(self):
        return self.court_name

    @classmethod
    def check_availability(cls, court: "Court", booked_from: datetime.datetime, booked_to: datetime.datetime) -> bool:
        bookings = Booking.objects.filter(
            Q(court=court)
            & Q(
                Q(booked_from__range=[booked_from, booked_to])
                | Q(booked_to__range=[booked_from, booked_to])
            )
        )
        if  bookings.exists():
            raise ValidationError(f"Court is not available")

    def book(self, account: Account, booked_from: datetime.datetime, booked_to: datetime.datetime) -> "Booking":
        Court.check_availability(self, booked_from, booked_to)
        booking = Booking.objects.create(
            court = self,
            account = account,
            booked_from = booked_from,
            booked_to = booked_to
        )
        return booking



class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    booked_from = models.DateTimeField()
    booked_to = models.DateTimeField()
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.booking_id)
    
    class Meta:
        unique_together = ("court", "booked_from", "booked_to")


    def clean(self):
        super().clean()
        Court.check_availability(self.court, self.booked_from, self.booked_to)

    def save(self, *args, **kwargs):
        Court.check_availability(self.court, self.booked_from, self.booked_to)
        super().save(*args, **kwargs)

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    booking_refrence = models.ForeignKey(Booking, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=200)
    card_expiry_date = models.CharField(max_length=200)
    CVV_code = models.CharField(max_length=200)

    def __str__(self):
        return str(self.transaction_date)





  



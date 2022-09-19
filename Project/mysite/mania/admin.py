from django.contrib import admin
from .models import Court
from .models import Account
from .models import Booking
from .models import Payment
# Register your models here.


admin.site.register(Court)
admin.site.register(Account)
admin.site.register(Booking)
admin.site.register(Payment)


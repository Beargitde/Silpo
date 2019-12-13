from django.contrib import admin
from .models import QRcode, QRzone, Feedback
# Register your models here.
admin.site.register(Feedback)
admin.site.register(QRcode)
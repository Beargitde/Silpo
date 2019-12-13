from django.db import models

class QRcode(models.Model):
    image = models. ImageField(upload_to='')

class QRzone(models.Model):
    name = models.CharField(max_length=120)



class Feedback(models.Model):
    qr_id = None
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=48)


# Create your models here.

from django.db import models


# Create your models here.

class Hotel(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    jumlah_review = models.IntegerField()
    lokasi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama + ' - ' + self.lokasi
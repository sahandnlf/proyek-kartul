from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(null=True, blank=True)
    selesai = models.BooleanField(default=False)
    buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        ordering = ['selesai']

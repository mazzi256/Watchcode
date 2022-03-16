# from ipaddress import ip_address
import typing
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # type: ignore


class Nmap(BaseModel):

    target = models.CharField(max_length=255, default="127.0.0.1")  # type: ignore
    port_range = models.CharField(max_length=255, default="1-1024", null=True)  # type: ignore
    command = models.CharField(max_length=255, default="-v -sS -sV -sC -A -O")  # type: ignore
    response = models.JSONField(default=dict, editable=False)

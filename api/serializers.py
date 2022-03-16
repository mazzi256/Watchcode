from rest_framework import serializers
from .models import Nmap


class NmapSerializer(serializers.ModelSerializer[Nmap]):
    class Meta:
        model = Nmap
        fields = "__all__"

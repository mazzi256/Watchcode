from rest_framework import serializers
from .models import Nmap


class NmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nmap
        fields = "__all__"

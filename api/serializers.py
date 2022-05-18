from rest_framework import serializers
from .models import Nmap, Web_Subdomain


class NmapSerializer(serializers.ModelSerializer[Nmap]):
    class Meta:
        model = Nmap
        fields = "__all__"


class Web_SubdomainSerializer(serializers.ModelSerializer[Web_Subdomain]):
    class Meta:
        model = Web_Subdomain
        fields = "__all__"

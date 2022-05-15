from rest_framework import serializers
from .models import Nmap, WebCrawler


class NmapSerializer(serializers.ModelSerializer[Nmap]):
    class Meta:
        model = Nmap
        fields = "__all__"


class WebCrawlerSerializer(serializers.ModelSerializer[WebCrawler]):
    class Meta:
        model = WebCrawler
        fields = "__all__"

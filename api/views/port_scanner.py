import json
import os
from string import ascii_lowercase
from django.http import Http404
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import NmapSerializer
from api.models import Nmap
from rest_framework.response import Response
from rest_framework import status
import nmap as np
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


# Create your views here.
class NmapList(APIView):
    def get(self, request, format=None):
        nmaps = Nmap.objects.all()
        serializer = NmapSerializer(nmaps, many=True)
        return Response(serializer.data)

    # Generating scheema and showing fields in swagger ui
    @swagger_auto_schema(request_body=NmapSerializer)
    def post(self, request, format=None):
        serializer = NmapSerializer(data=request.data)
        nm = np.PortScanner()

        if serializer.is_valid():
            target = str(serializer.validated_data.get("target"))
            # ip_address = request.get("ip_address")
            command = str(serializer.validated_data.get("command"))
            print("++++++++++++++++++++++++++++", command)
            try:
                nm.scan(
                    hosts=target,
                    arguments=command,
                )
                results = (
                    nm.analyse_nmap_xml_scan(),
                )  # Returns all the reults from the scanned target
                nm.scan(hosts=target, arguments=command)
                serializer.save(response=results)
                return Response(results, status=status.HTTP_201_CREATED)

            except Exception as e:
                print("+++++++++++++++++++", e)
                if target.startswith(ascii_lowercase):
                    raise KeyError(e)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NmapDetail(APIView):
    def get_object(self, target):
        try:
            return Nmap.objects.filter(target=target).latest("id")
        except Nmap.DoesNotExist:
            raise Http404

    def get(self, request, target):
        result = self.get_object(target)
        serializer = NmapSerializer(result)
        return Response(serializer.data)

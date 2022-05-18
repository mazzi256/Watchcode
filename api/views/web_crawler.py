from inspect import ArgSpec
import json
from django.http import Http404

import requests
from rest_framework.views import APIView
from api.serializers import Web_SubdomainSerializer
from api.models import Web_Subdomain
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from api.helper import get_sub_domain


class CrawlerPost(APIView):
    def get(self, request: Request, format=None) -> Response:
        queryset = Web_Subdomain.objects.all()
        serializer = Web_SubdomainSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Web_SubdomainSerializer)  # type:ignore
    def post(self, request: Request, format=None) -> Response:
        serializer = Web_SubdomainSerializer(data=request.data)
        if serializer.is_valid():
            try:
                url = str(serializer.validated_data.get("target"))

                domains = get_sub_domain(url)
                serializer.save(response=domains)
                return Response(domains, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("something bad has happened", e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Web_SubdomainDetail(APIView):
    def get_objact(self, target: str):

        try:
            return Web_Subdomain.objects.get(target=target)
        except Web_Subdomain.DoesNotExist:
            raise Http404

    try:

        def get(self, request: Request, target: str, format=None) -> Response:
            obj = Web_Subdomain.objects.filter(target=target).last()

            serializer = Web_SubdomainSerializer(obj, many=False)
            return Response(serializer.data)

    except Exception as e:

        print("something bad has happened", e)


# class Web_SubdomainDetail(APIView):
#     queryset = Web_Subdomain.objects.all()

#     def get_object(self, target: str):
#         try:
#             return self.queryset.get(target=target)
#         except Web_Subdomain.DoesNotExist:
#             raise Http404

#     def get(self, request: Request, target: str):
#         result = self.get_object(target=target)[:-1]
#         serializer = Web_SubdomainSerializer(result)
#         return Response(serializer.data)

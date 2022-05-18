from typing import Any
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import port_scanner
from api.views import web_crawler

urlpatterns = [
    path("portscanner/", port_scanner.NmapList.as_view()),
    path("result/<str:target>/", port_scanner.NmapDetail.as_view()),
    path("sub-domain/", web_crawler.CrawlerPost.as_view()),
    path("subdomain/<str:target>", web_crawler.Web_SubdomainDetail.as_view()),
]

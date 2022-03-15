from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import port_scanner


urlpatterns = [
    path("portscanner/", port_scanner.NmapList.as_view()),
    path("result/<str:target>/", port_scanner.NmapDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

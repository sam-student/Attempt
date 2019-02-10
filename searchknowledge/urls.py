
from django.urls import path
from django.conf.urls import  url

from django.conf.urls import url

from .views import \
    (
        SearchKnowledgeProductView
     )

urlpatterns = [
    url(r'^$',SearchKnowledgeProductView.as_view(), name="query"),
]

from django.conf.urls import url
from . import views

app_name = "people"
urlpatterns = [url(r"^$", views.hello)]

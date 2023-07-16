from django.urls import include, path
from .views import ImportView


urlpatterns = [path("import/", ImportView.as_view())]

from django.urls import include, path
from .views import MyView


urlpatterns = [path("import/", MyView.as_view())]

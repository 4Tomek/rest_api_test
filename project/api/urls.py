from django.urls import include, path
from .views import ImportView, DetailModelView, DetailObjectView


urlpatterns = [
    path("import/", ImportView.as_view()),
    path("detail/<str:model_name>/", DetailModelView.as_view()),
    path("detail/<str:model_name>/<int:id>/", DetailObjectView.as_view()),
]

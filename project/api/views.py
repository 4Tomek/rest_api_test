from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import *
from api.models import *

from django.apps import apps

class ImportView(APIView):
    def get(self, request):
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        serializers = {
            "AttributeName": AttributeNameSerializer,
            "AttributeValue": AttributeValueSerializer,
            "Attribute": AttributeSerializer,
            "Product": ProductSerializer,
            "ProductAttributes": ProductAttributesSerializer,
            "Image": ImageSerializer,
            "ProductImage": ProductImageSerializer,
            "Catalog": CatalogSerializer,
            "CatalogProduct": CatalogProductSerializer,
            "CatalogAttribute": CatalogAttributeSerializer,
        }

        try:
            for item in request.data:
                for key, serializer_class in serializers.items():
                    if key in item:
                        serializer = serializer_class(data=item[key])
                        if serializer.is_valid():
                            serializer.save()
                        break
            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DetailModelView(APIView):
    def get(self, request, model_name):
        model_name = model_name.lower()
        model_class = apps.get_model('api', model_name.capitalize())
        serializer_class = globals()[f"{model_name.capitalize()}Serializer"]

        if model_class and serializer_class:
            instances = model_class.objects.all()
            serializer = serializer_class(instances, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"res": "Model with this name does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class DetailObjectView(APIView):
    def get(self, request, model_name, id):
        model_name = model_name.lower()
        model_class = apps.get_model('api', model_name.capitalize())
        serializer_class = globals()[f"{model_name.capitalize()}Serializer"]

        if model_class and serializer_class:
            try:
                instance = model_class.objects.get(id=id)
                serializer = serializer_class(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except model_class.DoesNotExist:
                return Response({"res": "Object with this id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"res": "Model with this name does not exist"}, status=status.HTTP_400_BAD_REQUEST)

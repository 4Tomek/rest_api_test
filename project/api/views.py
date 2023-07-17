from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import *
from api.models import *


class ImportView(APIView):
    def get(self, request):
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        try:
            for i in request.data:
                if "AttributeName" in i.keys():
                    parameters = i["AttributeName"]
                    serializer = AttributeNameSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "AttributeValue" in i.keys():
                    parameters = i["AttributeValue"]
                    serializer = AttributeValueSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "Attribute" in i.keys():
                    parameters = i["Attribute"]
                    serializer = AttributeSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "Product" in i.keys():
                    parameters = i["Product"]
                    serializer = ProductSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "ProductAttributes" in i.keys():
                    parameters = i["ProductAttributes"]
                    serializer = ProductAttributesSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "Image" in i.keys():
                    parameters = i["Image"]
                    serializer = ImageSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "ProductImage" in i.keys():
                    parameters = i["ProductImage"]
                    serializer = ProductImageSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()
                elif "Catalog" in i.keys():
                    parameters = i["Catalog"]
                    serializer = CatalogSerializer(data=parameters)
                    if serializer.is_valid():
                        serializer.save()

                    for i in parameters["products_ids"]:
                        serializer = CatalogProductSerializer(
                            data={"product": i, "catalog": parameters["id"]}
                        )
                        if serializer.is_valid():
                            serializer.save()

                    for i in parameters["atributes_ids"]:
                        serializer = CatalogAttributeSerializer(
                            data={"attribute": i, "catalog": parameters["id"]}
                        )
                        if serializer.is_valid():
                            serializer.save()

            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class DetailModelView(APIView):
    def get(self, request, model_name):
        if model_name == "attributename":
            models = AttributeName.objects.all()
            serializer = AttributeNameSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "attributevalue":
            models = AttributeValue.objects.all()
            serializer = AttributeValueSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "attribute":
            models = Attribute.objects.all()
            serializer = AttributeSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "product":
            models = Product.objects.all()
            serializer = ProductSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "productatributes":
            models = ProductAttributes.objects.all()
            serializer = ProductAttributesSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "image":
            models = Image.objects.all()
            serializer = ImageSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "productimage":
            models = Image.objects.all()
            serializer = ProductImageSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif model_name == "catalog":
            models = Catalog.objects.all()
            serializer = CatalogSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"res": "Model with this name does not exist"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class DetailObjectView(APIView):
    def get(self, request, model_name, id):
        if model_name == "attributename":
            try:
                object = AttributeName.objects.get(id=id)
                serializer = AttributeNameSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "attributevalue":
            try:
                object = AttributeValue.objects.get(id=id)
                serializer = AttributeValueSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "attribute":
            try:
                object = Attribute.objects.get(id=id)
                serializer = AttributeSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "product":
            try:
                object = Product.objects.get(id=id)
                serializer = ProductSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "productattributes":
            try:
                object = ProductAttributes.objects.get(id=id)
                serializer = ProductAttributesSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "image":
            try:
                object = Image.objects.get(id=id)
                serializer = ImageSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "productimage":
            try:
                object = ProductImage.objects.get(id=id)
                serializer = ProductImageSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif model_name == "catalog":
            try:
                object = Catalog.objects.get(id=id)
                serializer = CatalogSerializer(object, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"res": "Object with this id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"res": "Model with this name does not exist"},
            status=status.HTTP_400_BAD_REQUEST,
        )

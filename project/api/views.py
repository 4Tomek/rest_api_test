from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import (
    AttributeNameSerializer,
    AttributeValueSerializer,
    AttributeSerializer,
    ProductSerializer,
    ProductAttributesSerializer,
    ImageSerializer,
    ProductImageSerializer,
    CatalogSerializer,
)


class MyView(APIView):
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
                else:
                    pass

            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

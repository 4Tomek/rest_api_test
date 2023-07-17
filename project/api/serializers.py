from rest_framework import serializers
from api.models import *


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = "__all__"


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    products_ids = ProductSerializer(read_only=True, many=True)
    atributes_ids = AttributeSerializer(read_only=True, many=True)

    class Meta:
        model = Catalog
        fields = "__all__"


class CatalogProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogProduct
        fields = "__all__"


class CatalogAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogAttribute
        fields = "__all__"

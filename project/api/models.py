from django.db import models


class AttributeName(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True, null=True)
    kod = models.CharField(max_length=100, blank=True, null=True)
    zobrazit = models.BooleanField(blank=True, null=True)


class AttributeValue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hodnota = models.CharField(max_length=100, blank=True, null=True)


class Attribute(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(
        AttributeName, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    hodnota_atributu_id = models.ForeignKey(
        AttributeValue, on_delete=models.DO_NOTHING, blank=True, null=True
    )


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True, null=True)
    kod = models.TextField(blank=True, null=True)
    cena = models.CharField(max_length=100, blank=True, null=True)
    mena = models.CharField(max_length=100, blank=True, null=True)
    published_on = models.CharField(max_length=100, blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)


class ProductAttributes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    cena = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, blank=True, null=True
    )


class Image(models.Model):
    id = models.BigIntegerField(primary_key=True)
    obrazek = models.CharField(max_length=200, blank=True, null=True)


class ProductImage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    obrazek_id = models.ForeignKey(
        Image, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    nazev = models.CharField(max_length=100, blank=True, null=True)


class Catalog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True, null=True)
    obrazek_id = models.ForeignKey(
        Image, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    products_ids = models.ManyToManyField(Product, through="CatalogProduct")
    atributes_ids = models.ManyToManyField(Attribute, through="CatalogAttribute")


class CatalogProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING)


class CatalogAttribute(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING)

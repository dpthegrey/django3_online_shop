from django.db import models


class Category(models.Model):
    """
    The Category model consists of a name field and a unique slug field (unique implies the creation of an index).
    """
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    # A ForeignKey to the Category model. This is a one-to-many relationship: a product belongs to one category and a category contains multiple products.
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    # The name of the product.
    name = models.CharField(max_length=200, db_index=True)
    # The slug for this product to build beautiful URLs.
    slug = models.SlugField(max_length=200, db_index=True)
    # An optional product image.
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    # An optional description of the product.
    description = models.TextField(blank=True)
    # This field uses Python's decimal.Decimal type to store a fixed-precision decimal number. The maximum number of digits (including the decimal places) is set using the max_digits attribute and decimal places with the decimal_places attribute.
    # By using the Decimal type, you will avoid float rounding issues.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # A boolean value that indicates whether the product is available or not. It will be used to enable/disable the product in the catalog.
    available = models.BooleanField(default=True)
    # This field stores when the object was created.
    created = models.DateTimeField(auto_now_add=True)
    # This field stores when the object was last updated.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

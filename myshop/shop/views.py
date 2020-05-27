from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# A view to list all the products or filter products by a given product category.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # filter the QuerySet with available=True to retrieve only available products.
    products = Product.objects.filter(available=True)
    if category_slug:
      # use an optional category_slug parameter to optionally filter products by a given category.
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


# A view to retrieve and display a single product by ID.
def product_detail(request, id_slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

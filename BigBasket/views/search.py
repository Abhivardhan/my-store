from BigBasket.models import Product, Category
from django.shortcuts import redirect, render



def search_product(request,product_slug):
    string = " ".join(product_slug.split('-'))
    product=None
    temp = []
    categories = Category.objects.all()
    if string is not None:
        product = Product.objects.filter(name__icontains=string)

        temp = list(product)
        if temp == []:
            return render(request, 'BigBasket/search/no_results.html', {'product': product,'categories': categories})
        return render(request, 'BigBasket/search/results.html', {'product': product, 'categories': categories})

    # return render(request, 'BigBasket/search/results.html',{'product': product, 'categories': categories})

def search(request, **kwargs):
    query = dict(request.GET)
    str = '-'.join(list(query['q'][0].split()))
    return redirect('BigBasket:product_search',str)
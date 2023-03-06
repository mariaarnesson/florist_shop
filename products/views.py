from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Favourite
from .forms import ProductForm
from django.views.generic import ListView


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_favourite(request, product_id):
    user = get_object_or_404(User, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Favourite.objects.create(user=user, product=product)
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_favourite(request, product_id):

    user = get_object_or_404(User, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Favourite.objects.filter(product=product, user=user).delete()
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def favourite_list(request):

    user = get_object_or_404(User, user=request.user)
    all_Favourtes= WishList.objects.filter(user=user)
    template = 'base.html'
    context = {
        'all_Favourtes': all_Favourtes,
    }
    return render(request, template, context)


'''
@login_required
def favourites(request):
    """
    A view to return a user's favourites
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = profile.favourites.all()
    template = 'products/favourites.html'
    context = {
        'products': products,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def toggle_favourite(request, product_id):
    """
    Add or remove a product from a user's list of favourites. Responds to
    an ajax request made when heart icon is clicked.
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    data = {
        'is_favourite': profile.favourites.filter(pk=product_id).exists(),
        'is_authenticated': request.user.is_authenticated,
    }

    if profile.favourites.filter(pk=product_id).exists():
        profile.favourites.remove(product)
    else:
        profile.favourites.add(product)

    return JsonResponse(data)


def favourite_list(request):
    user = request.user
    product_favourite = user.favourite.all()
    context = {
        'product_favourite': product_favourite, 
    }
    return render(request, 'product/favourite_list.html', context)


def product_favourite(request, id):
    product = get_object_or_404(Product, pk=product_id)

    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())    
'''


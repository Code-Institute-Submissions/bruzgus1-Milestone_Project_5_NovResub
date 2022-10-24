from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import PositiveReviewForm, NegativeReviewForm

# Create your views here.


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

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


def positive_reviews_view(request, product_id):
    """ A view to show individual product positive reviews """

    product = get_object_or_404(Product, pk=product_id)
    positive_reviews = product.positive_reviews.order_by("-created_on")
    # Get the currently logged-in User.
    user = get_user(request)
    # Provide User as initial data to the form
    positive_review_form = PositiveReviewForm(initial={'name': user})

    if request.method == 'POST':
        positive_review_form = PositiveReviewForm(data=request.POST)
        if positive_review_form.is_valid():
            print(positive_review_form.is_valid())
            positive_review_form.instance.name = request.user.username
            positive_review = positive_review_form.save(commit=False)
            positive_review.product = product
            positive_review.save()
        else:
            messages.error(request, "Your Positive Review was not submitted")

    template = 'products/positive_reviews.html'
    context = {
        'product': product,
        "positive_reviews": positive_reviews,
        "positive_review_form": positive_review_form,
    }

    return render(request, template, context)


def negative_reviews_view(request, product_id):
    """ A view to show individual product negative reviews """

    product = get_object_or_404(Product, pk=product_id)
    negative_reviews = product.negative_reviews.order_by("-created_on")
    # Get the currently logged-in User.
    user = get_user(request)
    # Provide User as initial data to the form
    negative_review_form = NegativeReviewForm(initial={'name': user})

    if request.method == 'POST':
        negative_review_form = NegativeReviewForm(data=request.POST)
        if negative_review_form.is_valid():
            print(negative_review_form.is_valid())
            negative_review_form.instance.name = request.user.username
            negative_review = negative_review_form.save(commit=False)
            negative_review.product = product
            negative_review.save()
        else:
            messages.error(request, "Your negative Review was not submitted")

    template = 'products/negative_reviews.html'
    context = {
        'product': product,
        "negative_reviews": negative_reviews,
        "negative_review_form": negative_review_form,
    }

    return render(request, template, context)

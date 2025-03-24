from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from django.db.models import Q
from product.models import Product, Category


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = "includes/navbar.html"

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    template_name = "product/products_list.html"
    queryset = Product.objects.all()
    context_object_name = "object_list"
    paginate_by = 12  # Optional pagination

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # Get all filter parameters
        search_query = request.GET.get('q')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')

        # Apply search filter
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__title__icontains=search_query)
            ).distinct()

        # Apply price filter
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        # Apply color filter
        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()

        # Apply size filter
        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        # Add search context
        context['search_query'] = request.GET.get('q', '')
        context['results_count'] = context['object_list'].count()

        # Preserve filter parameters
        context['min_price'] = request.GET.get('min_price', '')
        context['max_price'] = request.GET.get('max_price', '')
        context['selected_colors'] = request.GET.getlist('color')
        context['selected_sizes'] = request.GET.getlist('size')

        return context


from django.urls import path
from .views import product, checkout, HomeListView

app_name = 'core'


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),

    path('product/', product.as_view(), name='product')
]

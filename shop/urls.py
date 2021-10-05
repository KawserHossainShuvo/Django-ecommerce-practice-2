from django.urls import path
from .views import home, add_to_cart
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    path('', home, name='home'),
    # path('', HomeListView.as_view(), name='home'),
    # path('product/', ProductListView.as_view(), name='product'),
    path('add_to_cart/', add_to_cart, name='add-to-cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

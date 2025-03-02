from django.urls import path
from .views import ProducFormView, ProductListView
urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('agregar/', ProducFormView.as_view(), name ="add_product"),
]

from django.urls import path
from .views import get_user_orders, index

urlpatterns = [
    path('', index, name='index'),
    path('orders/<int:user_id>/<int:days_ago>/', get_user_orders, name='get_user_orders'),
]

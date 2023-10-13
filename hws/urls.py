from django.urls import path
from .views import get_user_orders, index, upload_image

urlpatterns = [
    path('', index, name='index'),
    path('orders/<int:user_id>/<int:days_ago>/', get_user_orders, name='get_user_orders'),
    path('img_form/', upload_image, name='upload_image'),
]

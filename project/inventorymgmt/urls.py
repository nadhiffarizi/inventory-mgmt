from django.urls import path
from .views import *

urlpatterns = [
    # include my path here
    path('', view=home_view, name='home'),
    path('create/', view=product_create_view, name='product_create'),
    path('list/', view=product_list_view, name='product_list'),
    path('update/<int:product_id>/', view=product_update_view, name='product_update'),
    path('delete/<int:product_id>/', view=product_delete_view, name='product_delete'),

]
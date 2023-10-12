from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, decrement_item, increment_item, remove_item, edit_item, get_item_json, add_item_ajax, remove_item_ajax, get_total_products

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    # Tugas 4
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('decrement_item/<int:id>', decrement_item, name='decrement_item'),
    path('increment_item/<int:id>', increment_item, name='increment_item'),
    path('remove_item/<int:id>', remove_item, name='remove_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    # Tugas 6
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('remove_item_ajax/<int:id>', remove_item_ajax, name='remove_item_ajax'),
    path('get_total_products', get_total_products, name='get_total_products'),
]
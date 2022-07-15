from django.contrib import admin
from django.urls import path, include

from food_delivery_app import views, admin_views, restaurant_views, user_views

# admin_patterns = [
#     path('', admin_views.default_path),
#     path('add-restaurant/', admin_views.add_restaurant),
#     # path('add-restaurant-manager', admin_views.add_restaurant_manager),
#     path('delete-restaurant/', admin_views.delete_restaurant)
# ]

restaurant_patterns = [
    path('', restaurant_views.restaurant_info, name='restaurant-home'),
    path('add-dish/', restaurant_views.add_dish, name='add-dish'),
    path('modify-dish/<int:dish_id>/', restaurant_views.modify_dish, name='modify-dish'),
    path('dishes/', restaurant_views.list_restaurant_dishes, name='dishes')

]

user_patterns = [
    path('', user_views.list_all_dishes, name='user-home'),
    #path('add-user/', user_views.add_user),
    path('search-restaurant/', user_views.search_restaurant),
    path('search-dish-in-restaurant/', user_views.search_dish_in_restaurant),
    path('search-dish/', user_views.search_dish_across_restaurants),
    path('place-order/', user_views.place_order)
]

urlpatterns = [
    path('', views.food_delivery_app_home),
    # path('admin/', include(admin_patterns)),
    path('restaurant/<int:restaurant_id>/', include(restaurant_patterns)),
    path('user/', include(user_patterns))
]
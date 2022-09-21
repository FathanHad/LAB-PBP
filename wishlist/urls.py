from django.urls import path
from wishlist.views import JSON_by_id, show_wishlist
from wishlist.views import XML_wishlist
from wishlist.views import JSON_wishlist
from wishlist.views import JSON_by_id, XML_by_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', XML_wishlist, name='XML_wishlist'),
    path('json/', JSON_wishlist, name='JSON_wishlist'),
    path('json/<int:id>', JSON_by_id, name='JSON_by_id'),
    path('xml/<int:id>', XML_by_id, name='XML_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
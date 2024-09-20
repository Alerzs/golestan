from django.urls import path    
from envahed.views import *

urlpatterns = [
    path('chose_dars/', Chose_Dars.as_view(), name='chose_dars'),
    path('edit_dars/<int:dars_id>/', edit_dars, name='edit_dars'),
    path('show_dars/', show_dars, name='show_dars'),
    path('delete_dars/<int:dars_id>/', delet_dars, name='delete_dars'),
    path('add_dars/', show_all_dars, name='show_all_dars'),
]
from django.urls import path
from .import views

urlpatterns=[
    path('',views.pet_add,name='pet_add'),
    path('pet_list/',views.pet_list,name='pet_list'),
    path('del_pet/<int:pet_id>/',views.del_pet,name='del_pet'),
    path('edit_pet/<int:pet_id>/',views.edit_pet,name='edit_pet'),

]
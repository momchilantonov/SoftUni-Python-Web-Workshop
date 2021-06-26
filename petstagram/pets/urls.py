from django.urls import path
from petstagram.pets.views import pet_details, like_pet, pets_list

urlpatterns = [
    path('', pets_list, name='pets list'),
    path('detail/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
]

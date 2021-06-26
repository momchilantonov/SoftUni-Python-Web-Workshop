from django.urls import path
from petstagram.pets.views import pet_details, like_pet, pets_list, create_pet, edit_pet, delete_pet, comment_pet

urlpatterns = [
    path('', pets_list, name='pets list'),
    # path('', ListPetsView.as_view(), name='list pets'), work with Base View
    path('detail/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),

]

from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like


def pets_list(req):
    all_pets = Pet.objects.all()
    context = {
        'all_pets': all_pets
    }
    return render(req, 'pet_list.html', context)


def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
    }
    return render(req, 'pet_detail.html', context)


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pet.id)

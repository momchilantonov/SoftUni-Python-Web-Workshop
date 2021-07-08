from django.shortcuts import render, redirect
from django.views.generic import ListView
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet, Like


def show_form(req, form, temp):
    context = {
        'form': form
    }
    return render(req, temp, context)


def save_form(req, form, temp, red):
    if form.is_valid():
        form.save()
        return redirect(red)
    return show_form(req, form, temp)


def get_pet_by_id(pk):
    return Pet.objects.get(pk=pk)


def pets_list(req):
    all_pets = Pet.objects.all()
    context = {
        'all_pets': all_pets
    }
    return render(req, 'pet_list.html', context)


# Example of Base View
class ListPetsView(ListView):
    template_name = 'pet_list.html'
    model = Pet
    context_object_name = 'pets'


# def pet_details(req, pk):
#     pet = Pet.objects.get(pk=pk)
#     pet.likes_count = pet.like_set.count()
#     comment_form = CommentForm()
#     comments = pet.comment_set.all()
#     context = {
#         'pet': pet,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(req, 'pet_detail.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
    }

    return render(request, 'pet_detail.html', context)


# With logic here in viwes
# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             comment=form.cleaned_data['comment'],
#             pet=pet,
#         )
#         comment.save()
#
#     return redirect('pet details', pet.id)


# With logic forms
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('pet details', pk)


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pet.id)


def create_pet(req):
    temp = 'pet_create.html'
    red = 'pets list'
    if req.method == "GET":
        form = PetCreateForm()
        return show_form(req, form, temp)
    form = PetCreateForm(req.POST, req.FILES)
    return save_form(req, form, temp, red)


def edit_pet(req, pk):
    temp = 'pet_edit.html'
    red = 'pets list'
    pet = get_pet_by_id(pk)
    if req.method == "GET":
        form = PetEditForm(initial=pet.__dict__)
        return show_form(req, form, temp)
    form = PetEditForm(
        req.POST,
        req.FILES,
        instance=pet,
    )
    return save_form(req, form, temp, red)


def delete_pet(req, pk):
    temp = 'pet_delete.html'
    red = 'pets list'
    pet = get_pet_by_id(pk)
    if req.method == "GET":
        context = {
            'pet': pet
        }
        return render(req, temp, context)
    pet.delete()
    return redirect(red)

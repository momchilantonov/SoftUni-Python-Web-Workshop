from django.contrib.auth.decorators import login_required
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


def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    is_owner = pet.user == req.user
    is_liked = pet.like_set.filter(user_id=req.user.id).exists()
    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked,
    }

    return render(req, 'pet_detail.html', context)


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
@login_required
def comment_pet(req, pk):
    form = CommentForm(req.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = req.user
        comment.save()

    return redirect('pet details', pk)


@login_required
def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like_by_user = pet.like_set.filter(user_id=req.user.id).first()
    if like_by_user:
        like_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=req.user,
        )
        like.save()
    return redirect('pet details', pet.id)


@login_required
def create_pet(req):
    if req.method == 'POST':
        form = PetCreateForm(req.POST, req.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = req.user
            pet.save()
            return redirect('pets list')
    else:
        form = PetCreateForm()

    context = {
        'form': form,
    }

    return render(req, 'pet_create.html', context)


@login_required
def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == 'POST':
        form = PetEditForm(req.POST, req.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets list')
    else:
        form = PetEditForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(req, 'pet_edit.html', context)


@login_required
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

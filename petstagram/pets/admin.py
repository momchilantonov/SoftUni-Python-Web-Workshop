from django.contrib import admin
from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'age', 'description', 'image', 'pet_likes']

    @staticmethod
    def pet_likes(obj):
        return obj.like_set.count()

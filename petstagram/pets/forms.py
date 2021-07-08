import os
from os.path import join

from django import forms
from django.conf import settings

from petstagram.pets.models import Pet


# class BootstrapFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_fields()
#
#     def _init_bootstrap_fields(self):
#         for _, field in self.fields.items():
#             if 'class' not in field.widget.attrs:
#                 field.widget.attrs['class'] = ''
#             field.widget.attrs['class'] += ' form-control'


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2'
                }
            )
        }


class PetEditForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['type'].widget.attrs.update({'readonly': 'readonly'})

    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)
        if commit:
            # os.remove(join(settings.MEDIA_ROOT, db_pet.image.url[len('/media/'):]))
            os.remove(join(settings.MEDIA_ROOT, str(db_pet.image)))
        return super().save(commit)

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly,'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2'
                }
            )
        }

# class PetDeleteForm(PetCreateForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for _, field in self.fields.items():
#             field.widget.attrs['disabled'] = 'disabled'
#             # field.widget.attrs['readonly'] = 'readonly'

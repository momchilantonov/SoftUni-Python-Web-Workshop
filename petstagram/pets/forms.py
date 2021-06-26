from django import forms
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
            'image_url': forms.URLInput(
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
            'image_url': forms.URLInput(
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

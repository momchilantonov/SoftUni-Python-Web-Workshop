from django.db import models

"""
In the models.py file create the Pet model. Each pet should have:
    • type – some of the following: "cat", "dog", "parrot"; max length = 6
    • name – max length = 6
    • age – positive number
    • description – text field
    • image_url – URL field
Now in the models.py file create Like model. Each like should have:
    • pet – foreign key to a Pet
Let us also register our models in the admin.py file in the app, so we can see it in the django admin
"""


class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    PARROT = 'parrot'
    CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
    ]
    type = models.CharField(
        max_length=6,
        choices=CHOICES,
    )
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pets')


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)



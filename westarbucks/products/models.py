from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

class Categories(models.Model):
    menu_id = models.ForeignKey('Menu', on_delete = models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Products(models.Model):
    category_id = models.ForeignKey('Categories', on_delete = models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length = 45)
    description = models.TextField()
    nutrition_id = models.ForeignKey('Nutritions', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.korean_name


class Images(models.Model):
    image_url = models.CharField(max_length = 2000)
    drink_id = models.ForeignKey('Products', on_delete = models.CASCADE)

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

class Allergy_Drink(models.Model):
    allergy_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink_id = models.ForeignKey('Products', on_delete=models.CASCADE)
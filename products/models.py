from email.mime import image
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# class 첫 글자는 대문자로 작성

class Menu(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length = 50)
    # on_delete 옵션은 ForeignKeyField가 바라보는 값이 삭제될 때 처리하는 방법을 지정해준다
    # CASCADE는 바라보는 값이 삭제될 때 fk를 포함하는 모델 인스턴스도 같이 삭제한다
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE) # Menu class 연결

    class Meta:
        db_table = 'categorise'

class Drink(models.Model):
    name_ko = models.CharField(max_length = 50) # 제품 이름
    name_en = models.CharField(max_length = 200) # 제품 이름
    description = models.TextField(max_length = 2000)
    category = models.ForeignKey('Category', on_delete = models.CASCADE) # Category class 연결
    nutrition = models.ForeignKey('Nutrition', on_delete = models.CASCADE) # Nutrition class 연결
    # 다:다 관계는 many to many 필드 사용 / through = '중간 필드 이름' 
    allergy = models.ManyToManyField('Allergy', through = 'Allergy_product' ) # Allergy_food class 연결
    
    class Meta :
        db_table = 'drinks'

class Image(models.Model):
    # 이미지?어떻게 처리하지?..? 링크로?
    image_url = models.CharField(max_length = 3000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta : 
        db_table = 'images'

class Nutrition(models.Model):
    calories_kacl = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    sodium_mg = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    sugars_g = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    caffein_mg = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    protein_g = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    fat_g = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)

    class Meta : 
        db_table = 'nutritions' 

class Allergy(models.Model):
    name = models.CharField(max_length = 40)

    class Meta : 
        db_table = 'allergies'

class Allergy_product(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE, null = True) # Allergy class 연결
    drink = models.ForeignKey('Drink', on_delete = models.CASCADE) # Product class 연결

    class Meta : 
        db_table = 'allergies_food'
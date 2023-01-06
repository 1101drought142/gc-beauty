from django.db import models

# Create your models here.
class ItemCategories(models.Model):

    father_categorie = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Родительская категория")

    name = models.CharField(max_length=30, verbose_name = "Название категории")
    slug = models.CharField(max_length=30, verbose_name = "Сокращение для ссылки")
    description = models.TextField(verbose_name = "Описание")


    picture = models.FileField(upload_to='uploads/', verbose_name = "Фотография")
    sort = models.IntegerField(verbose_name = "Индекс сортировки")


    Meta_title = models.CharField(max_length=30, verbose_name = "meta title категории")
    Meta_description = models.CharField(max_length=120, verbose_name = "meta description категории")
    Meta_keywords = models.CharField(max_length=60, verbose_name = "meta keywords категории")

    def __str__(self) -> str:
        return self.name
    
class Photos(models.Model):
    picture = models.FileField(upload_to='uploads/', verbose_name = "Фотография")
    item = models.ForeignKey("Item", on_delete=models.SET_NULL, blank=True, null=True)


class Item(models.Model):

    father_categorie = models.ForeignKey("ItemCategories", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Родительская категория")
    tags = models.ForeignKey("Tags", on_delete=models.SET_NULL, blank=True, null=True)
    types = models.ForeignKey("Types", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Тип")

    main_picture = models.FileField(upload_to='uploads/', verbose_name = "Основаня фотография", default="/")
    sort = models.IntegerField(verbose_name = "Индекс сортировки")
    name = models.CharField(max_length=30, verbose_name="Имя")
    slug = models.CharField(max_length=30, verbose_name="Сокрщение для ссылки")
    description = models.TextField(verbose_name="Описание")
    compound = models.TextField(verbose_name="Состав")
    properties = models.TextField(verbose_name="Характеристики")
    price = models.IntegerField(verbose_name="Цена")
    
    similar_items = models.ManyToManyField("self", blank=True, null=True, verbose_name="Похожие товары")

    Meta_title = models.CharField(max_length=30, verbose_name = "meta title товара")
    Meta_description = models.CharField(max_length=120, verbose_name = "meta description товара")
    Meta_keywords = models.CharField(max_length=60, verbose_name = "meta keywords товара")

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    
    name = models.CharField(max_length=30, verbose_name="Имя")
    mail = models.CharField(max_length=60, verbose_name="Email")
    phone = models.CharField(max_length=60, verbose_name="Телефон")
    city = models.CharField(max_length=60, verbose_name="Город")
    street = models.CharField(max_length=60, verbose_name="Улица")
    index = models.IntegerField(verbose_name="Индекс")
    house = models.IntegerField(verbose_name="Номер дома")
    flat = models.IntegerField(verbose_name="Номер квартиры")


    

       
"""
class OrderItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Товар")
    quantity = models.IntegerField(verbose_name="Количество")

"""

class CallbackForm(models.Model):
    name = models.CharField(max_length = 63)
    phone = models.CharField(max_length = 25)
    created_time = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.created_time) + " " + self.name

class Types(models.Model):
    name = models.CharField(max_length=30)
    father_categorie = models.ForeignKey("ItemCategories", on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=30)
    father_categorie = models.ForeignKey("ItemCategories", on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.FileField(upload_to='uploads/')


class Certificates(models.Model):
    name = models.CharField(max_length=60)
    photo = models.FileField(upload_to='uploads/')
    pdf_file = models.FileField(upload_to='uploads/')

class Banners(models.Model):
    name = models.CharField(max_length=60)
    small_description = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    link = models.CharField(max_length=30)

    desktop_photo = models.FileField(upload_to='uploads/')
    mobile_photo = models.FileField(upload_to='uploads/')
from django.db import models

# Create your models here.

class Card(models.Model):
    
    title = models.CharField(verbose_name="Название маршрута", max_lenght=50)
    description = models.TextField(verbose_name="Описание маршрута")
    price = models.IntegerField(verbose_name="Цена", default=1000)
    days_of_departure = models.CharField(verbose_name="Дата(ы) отправления",
            max_lenght=50)
    count_of_click_by_card = models.IntegerField(verbose_name="Сколько раз нажали")


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name']

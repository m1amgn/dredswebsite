from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя', blank=True, null=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон', blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_timestamp)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат айди')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
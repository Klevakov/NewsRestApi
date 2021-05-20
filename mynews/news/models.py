from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class News(models.Model):
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    title = models.CharField(verbose_name='Заголовок новости', max_length=200)
    news_text = models.TextField(verbose_name='Текст новости')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

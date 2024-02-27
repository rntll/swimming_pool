from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="Пользователь")
    is_superuser = models.BooleanField('Администратор', default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Info(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
    age = models.IntegerField()  # Числовое поле для возраста
    date_of_birth = models.DateField()  # Поле для даты рождения
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", default='')  # Поле для номера телефона
    SWIMMING_LEVEL_CHOICES = [
        ('Начинающий', 'Начинающий'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'),
    ]
    swimming_level = models.CharField(max_length=20, choices=SWIMMING_LEVEL_CHOICES)

    def __str__(self):
        return str(self.user_profile)

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
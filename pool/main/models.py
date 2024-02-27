from django.db import models

class Instructors(models.Model):
    name = models.CharField('ФИО', max_length=50)
    specialization = models.CharField('Специализация', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'

class AboutPool(models.Model):
    title = models.CharField('Название бассейна', max_length=50)
    description = models.CharField('Описание', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О бассейне'
        verbose_name_plural = 'О бассейне'


class WeekDay(models.Model):
    name = models.CharField('Название дня', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

class Schedule(models.Model):
    day = models.ForeignKey(WeekDay, on_delete=models.CASCADE, verbose_name='День недели')
    time = models.TimeField('Время')
    instructor = models.ForeignKey(Instructors, verbose_name='Инструктор', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day} - {self.time}'

    class Meta:
        verbose_name = 'Расписание занятий'
        verbose_name_plural = 'Расписание занятий'
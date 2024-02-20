from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Исполнитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Task(models.Model):
    priority_choices = [
        ('1', 'Very important task'),
        ('2', 'Task'),
        ('3', 'Task which can wait'),
    ]

    title = models.CharField(max_length=80, verbose_name='Заголовок')
    comment = models.TextField(verbose_name='Комментарий к задаче')
    priority = models.CharField(max_length=40,
                                default=priority_choices[1],
                                choices=priority_choices,
                                db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    executor = models.ForeignKey(Executor, on_delete=models.PROTECT)

    def __str__(self):
        return f'Task {self.title}, priority: {self.priority}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

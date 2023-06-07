from django.db import models


# Create your models here.
class ServiceModels(models.Model):
    description = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    cost = models.IntegerField()
    image = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.id}&{self.name}"

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ('cost',)


class TaskModels(models.Model):
    description = models.CharField(max_length=5000)
    name = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.id}&{self.name}"

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ('-id',)


class SolutionModels(models.Model):
    description = models.CharField(max_length=5000)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}&{self.name}"

    class Meta:
        verbose_name = "solution"
        verbose_name_plural = "solutions"
        ordering = ('-id',)


class UserModels(models.Model):
    surname = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=225)
    current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}&{self.surname}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ('id',)


class ScheduleTopicModels(models.Model):
    date = models.CharField(max_length=30)
    title = models.CharField(max_length=225)
    level = models.IntegerField()

    def __str__(self):
        return f"{self.id}&{self.title}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"
        ordering = ('date', 'level')

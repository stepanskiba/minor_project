from django.db import models


class SumMoney(models.Model):
    task = models.CharField("Формулировка задачи",
                            default="1006. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и монетой 2 руб., если это возможно.",
                            max_length=255)
    S = models.IntegerField("Денежная сумма", default=0,)
    current_date = models.DateTimeField("Дата изменения(save)", auto_now=True)

    def __str__(self):
        return f"{self.id}&{self.task}"

    class Meta:
        verbose_name = "S"
        verbose_name_plural = "S"
        ordering = ('-id', '-S')

# python manage.py makemigrations
# python manage.py migrate

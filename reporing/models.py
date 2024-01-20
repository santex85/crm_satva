from django.db import models


class Reports(models.Model):
    REPORT_TYPE_CHOICES = (
        ('INCOME', 'По доходам'),
        ('EXPENSE', 'Расходам'),
        ('CLIENT_PROFITABILITY', 'Доходности клиентов'),
        # добавьте другие типы отчетов по мере необходимости
    )
    id = models.AutoField(primary_key=True)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    report_date = models.DateTimeField(auto_now_add=True)
    report_content = models.TextField()

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return f"{self.id} ({self.report_type})"
